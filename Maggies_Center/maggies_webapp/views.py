from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user
from .forms import BaseUserForm, NewStaffForm, VisitForm, TempVisitNameMappingForm, ExportForm
from maggies_webapp.models import Visit, Activity, StaffMember, TempVisitNameMapping, Centre, ActivityName
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .stats import get_visitor_stats
from django.contrib import messages
from .util import Util
from django.http import HttpResponse
import datetime
import csv


@login_required
def main_page(request):
    staff_member = StaffMember.objects.get(user_mapping=request.user)
    centre = request.GET.get("centre", None)
    all_objects = []
    if centre is not None:
        centre = get_object_or_404(Centre, pk=centre)
        all_objects = TempVisitNameMapping.objects.filter(centre=centre)
    else:
        all_objects = TempVisitNameMapping.objects.all()
    staff_member = StaffMember.objects.all().get(user_mapping=request.user)
    activities = Activity.objects.all()
    context_dict = {"centres": staff_member.centre.all(),"activities":[]}
    day = datetime.date.today().weekday()
    for a in activities:
        for t in a.get_scheduled_times(day):
            pass
    values = []
    for visitor in all_objects:
        if Util.check_user_can_access(staff_member, visitor.related_visit):
            values += [Util.generate_dict_from_instance(visitor)]

    context_dict["visitors"] = values
    return render(request,'maggies/main.html', context_dict)


class AddUser(LoginRequiredMixin, View):

    def get(self, request):
        form_a = BaseUserForm()
        form_b = NewStaffForm()
        return render(request, "maggies/new_user.html", {"form_a": form_a,
                                                         "form_b": form_b})

    def post(self, request):
        form_a = BaseUserForm(request.POST)
        form_b = NewStaffForm(request.POST)
        if form_a.is_valid():
            if form_b.is_valid():
                new_user = User.objects.create_user(
                    username=form_a.cleaned_data["user"],
                    password=form_a.cleaned_data["password"],
                    email=form_a.cleaned_data["email"])
                new_prof = form_b.save(commit=False)
                new_prof.user_mapping = new_user
                new_prof.save()
            else:
                messages.warning(request, "Invalid user information")
        else:
            messages.warning(request, "Invalid user information")
        return render(request, "maggies/new_user.html", {"form_a": form_a,
                                                         "form_b": form_b})


class Schedule(LoginRequiredMixin, View):
    def get(self,request):
        context_dict = {}
        current_user = StaffMember.objects.get(user_mapping = get_user(request))
        context_dict["centres"] = current_user.centre.all()
        context_dict["activities"] = [{"name": Util.get_activity_name_in_user_lang(request.user, x),
                                       "id": x.pk} for x in Activity.objects.all()]
        return render(request,'maggies/schedule.html',context_dict)

    def post(self, request):
        data = request.POST
        activities = data.getlist("activity")
        number = len(activities)
        activity_dict = {}
        for i in range(0, number):
            if (activities[i] not in activity_dict):
                activity_dict[activities[i]] = {"times": [], "staff": []}
            activity_dict[activities[i]]["times"].append([data.getlist("start")[i], data.getlist("end")[i]])
            activity_dict[activities[i]]["staff"].append(data.getlist("staff")[i])

        for key in activity_dict:
            act = get_object_or_404(Activity, pk=data.get("activity"))
            act.centre = Centre.objects.get(name=data.get("centre"))
            act.set_scheduled_times(int(data.get("day")), activity_dict[key]["times"])
            act.save()
            for staff_member in activity_dict[key]["staff"]:
                act.instructed_by.add(StaffMember.objects.get(name=staff_member))
            act.save()
        return redirect('/schedule/')

class DeleteSchedule(View,LoginRequiredMixin):
    def get(self,request):
        context_dict = {}
        current_user = get_user(request)
        activities = Activity.objects.all()
        context_dict["activities"] = []
        for a in activities:
            context_dict["activities"].append(a)
        return render(request, 'maggies/delete_schedule.html',context_dict)

    def post(self,request):
        return redirect('/delactivity/')

class ShowSchedule(View,LoginRequiredMixin):
    def get(self,request,slug):
        context_dixt = {}
        activities = Activity.objects.all().filter(centre=Centre.objects.get(name=slug))
        activity_list = []
        for a in activities.all():
            activity_list.append(Util.get_activity_name_in_user_lang(get_user(request),a))
        print(activity_list)

class AddVisitor(LoginRequiredMixin, View):

    def get(self, request):
        this_id = request.GET.get("id", None)
        stats = get_visitor_stats()
        if this_id is not None:
            this_visit = get_object_or_404(Visit, pk=this_id)
            this_name = ""
            if not Util.check_user_obj_can_access(request.user, this_visit):
                return redirect("/")
            try:
                this_visit_meta = TempVisitNameMapping.objects.get(
                    related_visit__pk=this_id)
                this_name = this_visit_meta.visitor_name
            except:
                pass
            form_a = TempVisitNameMappingForm(initial={"visitor_name": this_name})
            form_b = VisitForm(instance=this_visit)
        else:
            form_a = TempVisitNameMappingForm()
            form_b = VisitForm(initial=stats, )

        return render(request, "maggies/new_visitor.html", {"form_a": form_a,
                                                            "form_b": form_b})

    def post(self, request):
        this_id = request.GET.get("id", None)
        old_visit = None
        if this_id is not None:
            old_visit = Visit.objects.get(pk=this_id)
            if not Util.check_user_obj_can_access(request.user, old_visit):
                return redirect("/")
        form_a = TempVisitNameMappingForm(request.POST)
        form_b = VisitForm(request.POST)
        if form_a.is_valid():
            if form_b.is_valid():
                new_mapping = form_a.save(commit=False)
                new_visitor = form_b.save()
                new_mapping.related_visit = new_visitor
                new_visitor.save()
                new_mapping.save()
                if this_id is not None:
                    new_visitor.timestamp = old_visit.timestamp
                    old_visit.delete()
                return redirect("/")
            else:
                messages.warning(request, "Invalid user information")
        else:
            messages.warning(request, "Invalid visitor information")
        return render(request, "maggies/new_visitor.html", {"form_a": form_a,
                                                            "form_b": form_b})


class Export(LoginRequiredMixin, View):

    def get(self, request):
        visits = Visit.objects.all()
        print(visits)
        form = ExportForm()
        return render(request, "maggies/export.html", {"form": form})

    def post(self, request):
        form = ExportForm(request.POST)
        if form.is_valid():
            startdate = form.cleaned_data["startdate"]
            enddate = form.cleaned_data["enddate"]
            center = form.cleaned_data["center"]
            visitors = Visit.objects.all().filter(timestamp__gte=startdate, timestamp__lte=enddate, visit_site=center)
            print(visitors)

            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="' + str(startdate) + '-' + str(enddate) + '-' + str(center) + '.csv"'

            writer = csv.writer(response)
            writer.writerow(['Timestamp', 'Journey Stage', 'Center Location', 'Nature of Visit', 'Cancer Type', 'Seen by', 'Visit Type', 'Activities'])
            for visitor in visitors:
                activities = ""
                for activity in visitor.activities.all():
                    activities += Util.get_activity_name_in_user_lang(request.user, activity) + ';'
                row = [str(visitor.timestamp), str(visitor.journey_stage), visitor.visit_site, visitor.nature_of_visit, visitor.cancer_site, visitor.seen_by, visitor.type, activities]
                writer.writerow(row)

            return response
        else:
            print("Export failed to retrieve input")
        return render(request, "maggies/export.html", {"form": form})
