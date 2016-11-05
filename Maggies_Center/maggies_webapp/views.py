from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from maggies_webapp.models import Visit
# Create your views here.


def login_page(request):
    html ='login page html'
    return HttpResponse(html)

def main_page(request):
    return render(request,'main_page.html')


def export(request):
    if (request.method) == 'GET':
        print("Received export request")
        print(request.GET.get('startdate'), request.GET.get('enddate'))
        visits = Visit.objects.all()
        print(visits)

