from django.shortcuts import render
from .models import about_cot
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def home(req):
    return render(req,'home.html')


def about(req):
    display = about_cot.objects.all()
    return render(req,'about.html',{'about':display})