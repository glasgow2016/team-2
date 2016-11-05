from django.shortcuts import render
from maggies_webapp import models

# Create your views here.

def login_page(request):
    return render(request, 'login.html')

def main_page(request):
    return render(request,'main_page.html')

def schedule(request):
    context_dict = {}
    context_dict["schedule"] = {}
    models.Activity.objects.filter()
    return render(request,'schedule.html',context_dict)
