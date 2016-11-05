from django.shortcuts import render
from maggies_webapp.models import Visit, Activity
# Create your views here.

def login_page(request):
    return render(request, 'login.html')

def main_page(request):
    return render(request,'main_page.html')

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
