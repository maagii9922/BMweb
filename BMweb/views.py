from django.http import HttpResponse
from django.shortcuts import render
from .models import Hereglegch


def login(request):
    h = Hereglegch.objects.all()
    print(h)
    return render(request,'login.html',{'hereglegch':h})