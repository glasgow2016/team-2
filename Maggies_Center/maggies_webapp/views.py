from django.shortcuts import render
from django.http import HttpResponse
from maggies_webapp import models
from django.contrib.auth import get_user
# Create your views here.


def login_page(request):
    html ='login page html'
    return HttpResponse(html)

def main_page(request):
    return render(request,'main_page.html')

def schedule(request):
    context_dict = {}
    current_user = models.StaffMember.objects.get(user_mapping = get_user(request))
    context_dict["schedule"] = {}
    for activity in models.Activity.objects.filter(centre=current_user.centre):
        for day in activity.scheduled_times_array:
            context_dict["schedule"][day] = {}
            context_dict["schedule"][day][activity.id] = []
            for time in activity.scheduled_times_array[day]:
                context_dict["schedule"][day][activity.id].append(time)

    models.Activity.objects.filter(centre="blah")
    return render(request,'schedule.html',context_dict)

