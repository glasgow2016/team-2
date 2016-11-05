from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import BaseUserForm, NewStaffForm
from maggies_webapp import models

from maggies_webapp.models import Visit, Activity
# Create your views here.

def login_page(request):
    return render(request, 'maggies/login.html')

def main_page(request):
    return render(request,'maggies/main_page.html')


class AddUser(View, LoginRequiredMixin):

    def get(self, request):
        form_a = BaseUserForm()
        form_b = NewStaffForm()
        return render("maggies/new_user.html")

    def post(self, request):
        pass


def schedule(request):
    context_dict = {}
    context_dict["schedule"] = {}
    Activity.objects.filter()
    return render(request,'schedule.html',context_dict)

def export(request):
    if (request.method) == 'GET':
        print("Received export request")
        print(request.GET.get('startdate'), request.GET.get('enddate'))
        visits = Visit.objects.all()
        print(visits)
