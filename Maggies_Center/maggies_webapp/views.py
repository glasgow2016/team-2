from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user
from .forms import BaseUserForm, NewStaffForm
from maggies_webapp.models import Visit, Activity, StaffMember
from django.http import HttpResponseNotFound
from django.contrib.auth.models import AnonymousUser
# Create your views here.

def main_page(request):
    return render(request,'maggies/main.html')


class AddUser(View, LoginRequiredMixin):

    def get(self, request):
        form_a = BaseUserForm()
        form_b = NewStaffForm()
        return render(request, "maggies/new_user.html")

    def post(self, request):
        pass


def schedule(request):
    context_dict = {}
    current_user = get_user(request)
    if (current_user.id == None):
        return HttpResponseNotFound('<p>Page not Found</p>')
    current_user = StaffMember.objects.get(user_mapping = get_user(request))
    context_dict["schedule"] = {}
    for activity in Activity.objects.filter(centre=current_user.centre):
        for day in activity.scheduled_times_array:
            context_dict["schedule"][day] = {}
            context_dict["schedule"][day][activity.id] = []
            for time in activity.scheduled_times_array[day]:
                context_dict["schedule"][day][activity.id].append(time)
    Activity.objects.filter(centre="blah")
    return render(request,'maggies/schedule.html',context_dict)

class Export(View, LoginRequiredMixin):

    def get(self, request):
        print("Received export request")
        print(request.GET.get('startdate'), request.GET.get('enddate'))
        visits = Visit.objects.all()
        print(visits)
