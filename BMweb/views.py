from BMweb.settings import AUTH_PASSWORD_VALIDATORS
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .models import Customer, Hereglegch,Paiz,State, HereglegchRole,Product,Manufacturer,ProdBrand,Company,Category
from django.views.generic import ListView
from .forms import HereglegchForm, CompanyForm, ProductForm,ProdType

# class CompanyListView(ListView):
#     model = Company

def home(request):
    return render(request,'home.html')

def hereglegch(request):
    # r = HereglegchRole(levelname = 'Бараа шинээр бүртгэх хүсэлт илгээх')
    # r.save()
    if request.method == 'GET':
        form = HereglegchForm()
        return render(request,'hereglegch.html', {'HereglegchForm': HereglegchForm})
    elif request.method == 'POST':
        p1 = request.POST['password']
        p2 = request.POST['password1']
        if(p1 == p2):
            h = Hereglegch(ovog= request.POST['ovog'], ner= request.POST['ner'], role=  HereglegchRole.objects.get(pk= int(request.POST['role']))  , company=  Company.objects.get(pk=int(request.POST['company'])), password= request.POST['password'])
            h.save()
            return render(request,'home1.html' )
        else:
            h = HereglegchForm(request.POST)
            return render(request,'hereglegch.html',{'HereglegchForm': h, "errmsg": "Нууц үг тохирохгүй байна."})

def hereglegchList(request):
    h = Hereglegch.objects.all()
    # print(h)
    return render(request,'hereglegchList.html',{'HereglegchList': h})

def company(request):
    # r = HereglegchRole(levelname = 'Бараа шинээр бүртгэх хүсэлт илгээх')
    # r.save()
    if request.method == 'GET':
        form = CompanyForm()
        return render(request,'company.html', {'CompanyForm': CompanyForm})
    elif request.method == 'POST':
        h = Company(comName= request.POST['comName'], hayag= request.POST['hayag'], phone= request.POST['phone'])
        h.save()
        return render(request,'home1.html' )

def companyList(request):
    c = Company.objects.all()
    return render(request, 'companyList.html',{'companyList': c})

def product(request):
    # r = HereglegchRole(levelname = 'Бараа шинээр бүртгэх хүсэлт илгээх')
    # r.save()
    if request.method == 'GET':
        form = ProductForm()
        return render(request,'product.html', {'ProductForm': ProductForm})
    elif request.method == 'POST':
        h = Product(
                prodName= request.POST['prodName'],
                zCode= request.POST['zCode'],
                prodType=  ProdType.objects.get(pk= int(request.POST['prodType'])),
                zzCode= request.POST['zzCode'],
                price= request.POST['price'],
                hemNegj= request.POST['hemNegj'],
                hudNegj= request.POST['hudNegj'],
                company=  Company.objects.get(pk= int(request.POST['company'])),
                erNershil= request.POST['erNershil'],
                emHelber= request.POST['emHelber'],
                paiz=  Paiz.objects.get(pk= int(request.POST['paiz'])),
                uildwerlegch= request.POST['uildwerlegch'],
                uNiiluulegch= request.POST['uNiiluulegch'],
                category=  Category.objects.get(pk= int(request.POST['category'])),
                borBoloh= request.POST['borBoloh'],
                hudAwch= request.POST['hudAwch'],
                state=  State.objects.get(pk= int(request.POST['state'])),
                )
        h.save()
        return render(request,'home1.html' )
        # form = ProductForm(request.POST)
        # print(request.POST)
        # if form.is_valid():
        #     h = Product(
        #         prodName= request.POST['prodName'],
        #         zCode= request.POST['zCode'],
        #         prodType=  ProdType.objects.get(pk= int(request.POST['prodType'])),
        #         zzCode= request.POST['zzCode'],
        #         price= request.POST['price'],
        #         hemNegj= request.POST['hemNegj'],
        #         hudNegj= request.POST['hudNegj'],
        #         company=  Company.objects.get(pk= int(request.POST['company'])),
        #         erNershil= request.POST['erNershil'],
        #         emHelber= request.POST['emHelber'],
        #         paiz=  Paiz.objects.get(pk= int(request.POST['paiz'])),
        #         uildwerlegch= request.POST['uildwerlegch'],
        #         uNiiluulegch= request.POST['uNiiluulegch'],
        #         category=  Category.objects.get(pk= int(request.POST['category'])),
        #         borBoloh= request.POST['borBoloh'],
        #         hudAwch= request.POST['hudAwch'],
        #         state=  State.objects.get(pk= int(request.POST['state'])),
        #         )
        #     h.save()
        #     return render(request,'home1.html' )
        # else:
        #     form = ProductForm()
        #     return render(request,'product.html', {'ProductForm': ProductForm})

def login(request):
    h = Hereglegch.objects.all()
    print(h)
    return render(request,'login.html',{'hereglegch':h})

def customer(request):
    c = Customer.objects.all()
    # print(h)
    return render(request,'login.html',{'customer':c})

def thanks(request):
    return HttpResponse('thanks')

def manufacturer(request):
    m = Manufacturer.objects.all()
    return render(request,'test.html', {'manufacturer': m})

def prodBrand(request):
    b = ProdBrand.objects.all()
    return render(request,'test.html', {'prodBrand': b})


# def get_name(request):
#     if request.method == 'GET':
#         dd =  request.session.get('err_msg')
#         ee =  request.session.get('formData') 
#         print(ee)
#         form = NameForm()  
#         if (ee is not None):
#             form = NameForm({"your_name": ee + "asdf"}) 
#         return render(request, 'test.html', {'form': form, 'err_msg':dd})
#     elif request.method == 'POST':     
#         # print(request.POST)   
#         # print(request.POST['your_name'])
#         # print(request.POST['your_name1'])
#         # print(request.POST['your_name2'])
#         # print(request.POST['your_name3'])
#         form = NameForm(request.POST)
#         if form.is_valid():
#             # return HttpResponse('/thanks/')
#             # return HttpResponseRedirect('/get_name/')\
#             # print(form.cleaned_data['your_name'])
#             request.session['err_msg'] = "aldaa"
#             request.session['formData'] = form.cleaned_data['your_name']
#             # form.err_msg = "asdfads"
#             return HttpResponseRedirect('/get_name/')\
#             # return HttpResponseRedirect('/thanks/')

#     # # if a GET (or any other method) we'll create a blank form
#     # else:
