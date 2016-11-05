from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import BaseUserForm, NewStaffForm

def login_page(request):
    html ='login page html'
    return HttpResponse(html)

def main_page(request):
    return render(request,'main_page.html')

class AddUser(View, LoginRequiredMixin):

    def get(self, request):
        form_a = BaseUserForm()
        form_b = NewStaffForm()
        return render("templates/new_")

    def post(self, request):
        pass
