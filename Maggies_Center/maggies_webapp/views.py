from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def login_page(request):
    html ='login page html'
    return HttpResponse(html)

def main_page(request):
    return render(request,'main_page.html')
