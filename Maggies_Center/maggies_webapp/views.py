from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import BaseUserForm, NewStaffForm
from maggies_webapp import models

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
    models.Activity.objects.filter()
    return render(request,'maggies/schedule.html',context_dict)
