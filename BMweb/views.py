from BMweb.settings import AUTH_PASSWORD_VALIDATORS
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .models import Customer, Hereglegch,Product,Manufacturer,ProdBrand,Company
from django.views.generic import ListView
from .forms import NameForm

class CompanyListView(ListView):
    model = Company

# def login(request):
#     h = Hereglegch.objects.all()
#     print(h)
#     return render(request,'login.html',{'hereglegch':h})

def customer(request):
    c = Customer.objects.all()
    # print(h)
    return render(request,'login.html',{'customer':c})

def get_name(request):
    if request.method == 'GET':
        dd =  request.session.get('err_msg')
        ee =  request.session.get('formData') 
        print(ee)
        form = NameForm()  
        if (ee is not None):
            form = NameForm({"your_name": ee + "asdf"}) 
        return render(request, 'test.html', {'form': form, 'err_msg':dd})
    elif request.method == 'POST':     
        # print(request.POST)   
        # print(request.POST['your_name'])
        # print(request.POST['your_name1'])
        # print(request.POST['your_name2'])
        # print(request.POST['your_name3'])
        form = NameForm(request.POST)
        if form.is_valid():
            # return HttpResponse('/thanks/')
            # return HttpResponseRedirect('/get_name/')\
            # print(form.cleaned_data['your_name'])
            request.session['err_msg'] = "aldaaa"
            request.session['formData'] = form.cleaned_data['your_name']
            # form.err_msg = "asdfads"
            return HttpResponseRedirect('/get_name/')\
            # return HttpResponseRedirect('/thanks/')

    # # if a GET (or any other method) we'll create a blank form
    # else:

def thanks(request):

    return HttpResponse('tanks')

def manufacturer(request):
    m = Manufacturer.objects.all()
    return render(request,'test.html', {'manufacturer': m})

def prodBrand(request):
    b = ProdBrand.objects.all()
    return render(request,'test.html', {'prodBrand': b})


