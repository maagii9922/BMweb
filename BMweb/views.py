from django.http import HttpResponse
from django.shortcuts import render
from .models import Customer, Hereglegch,Product,Manufacturer,ProdBrand
from .forms import NameForm

# def login(request):
#     h = Hereglegch.objects.all()
#     print(h)
#     return render(request,'login.html',{'hereglegch':h})

def customer(request):
    c = Customer.objects.all()
    # print(h)
    return render(request,'login.html',{'customer':c})

def get_name(request):
    # if request.method == 'POST':
    #     # create a form instance and populate it with data from the request:
    #     form = NameForm(request.POST)
    #     # check whether it's valid:
    #     if form.is_valid():
    #         # process the data in form.cleaned_data as required
    #         # ...
    #         # redirect to a new URL:
    #         return HttpResponse('/thanks/')

    # # if a GET (or any other method) we'll create a blank form
    # else:
    form = NameForm()

    return render(request, 'test.html', {'form': form})

def manufacturer(request):
    m = Manufacturer.objects.all()
    return render(request,'test.html', {'manufacturer': m})

def prodBrand(request):
    b = ProdBrand.objects.all()
    return render(request,'test.html', {'prodBrand': b})