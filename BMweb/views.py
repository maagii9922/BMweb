from django.http import HttpResponse
from django.shortcuts import render
from .models import Hereglegch

# def home(request):
#     b=Baraa.objects.all()
#     return render(request,'home.html',{'baraa':b})
# def home(request):
#     t=Tohirgoo.objects.all()
#     s=Tses.objects.all().order_by('-daraalal')
#     r=Rowtses.objects.all().order_by('-daraalal')
#     n=Shine.objects.all().order_by('-daraalal')
#     print (s)
#     return render(request,'home.html',{'tohirgoo':t,'tses':s,'rowtses':r,'shine':n})

def login(request):
    # return HttpResponse("ggdfgd")
    h = Hereglegch.objects.all()
    print(h)
    return render(request,'login.html',{'hereglegch':h})