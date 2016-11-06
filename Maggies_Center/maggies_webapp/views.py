from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user
from .forms import BaseUserForm, NewStaffForm, VisitForm, TempVisitNameMappingForm
from maggies_webapp.models import Visit, Activity, StaffMember, TempVisitNameMapping, Centre
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .stats import get_visitor_stats
from django.contrib import messages
from .util import Util

@login_required
def main_page(request):
    if request.user is None:
        return redirect('/accounts/login/')
    staff_member = StaffMember.objects.all().get(user_mapping=request.user)
    centers = Centre.objects.filter(staffmember=staff_member)
    values = []
    for visitor in TempVisitNameMapping.objects.all():
        if (visitor.related_visit.visit_site in centers):
            values += [Util.generate_dict_from_instance(visitor)]
    return render(request,'maggies/main.html', {'visitors': values})


class AddUser(View, LoginRequiredMixin):

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


class Schedule(View, LoginRequiredMixin):
    def get(self,request):
        context_dict = {}
        current_user = get_user(request)
        current_user = StaffMember.objects.get(user_mapping = get_user(request))
        context_dict["schedule"] = {}
        for activity in Activity.objects.filter(centre=current_user.centre):
            for i in range(0,7,1):
                context_dict["schedule"][i] = activity.scheduled_times_array[i]
                # context_dict["schedule"][day] = {}
                # context_dict["schedule"][day][activity.id] = []
                # for time in activity.scheduled_times_array[day]:
                #     context_dict["schedule"][day][activity.id].append(time)
        # Activity.objects.filter(centre="blah")
        return render(request,'maggies/schedule.html',context_dict)

    def post(self,request):
        data = request.POST
        activities = data.getlist("activity")
        number = len(activities)
        activity_dict = {}
        for i in range(0,number):
            activity_dict[activities[i]] = {"times":[]}
            activity_dict[activities[i]]["times"].append([data.getlist("start")[i],[data.getlist("end")[i]]])


            # act = Activity()
            # act.centre = StaffMember.objects.get(user_mapping = get_user(request)).centre
            # staff = data.getlist("name")[i]
            # if staff is not None:
            #     act.instructed_by = StaffMember.objects.get(name=data.getlist("name"))[i]
            # start = data.getlist("start")[i]
            # if start is not None:
            #     pass
            # print(start)
            # print(staff)
        print(activity_dict)
        return render(request,'maggies/schedule.html')


class AddVisitor(View, LoginRequiredMixin):

    def get(self, request):
        stats = get_visitor_stats()
        form_a = TempVisitNameMappingForm()
        form_b = VisitForm(initial=stats,)
        return render(request, "maggies/new_visitor.html", {"form_a": form_a,
                                                            "form_b": form_b})

    def post(self, request):
        form_a = TempVisitNameMappingForm(request.POST)
        form_b = VisitForm(request.POST)
        if form_a.is_valid():
            if form_b.is_valid():
                new_mapping = form_a.save(commit=False)
                new_visitor = form_b.save()
                new_mapping.related_visit = new_visitor
                new_visitor.save()
                new_mapping.save()
                return redirect("/")
            else:
                messages.warning(request, "Invalid user information")
        else:
            messages.warning(request, "Invalid visitor information")
        return render(request, "maggies/new_visitor.html", {"form_a": form_a,
                                                            "form_b": form_b})


class Export(View, LoginRequiredMixin):

    def get(self, request):
        print("Received export request")
        print(request.GET.get('startdate'), request.GET.get('enddate'))
        visits = Visit.objects.all()
        print(visits)
