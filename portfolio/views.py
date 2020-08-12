from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

def portfolio_home(request):
    projects = Project.objects.all()
    return render(request,'portfolio/portfolio_home.html',{'projects':projects})
