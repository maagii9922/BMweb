from BMweb.settings import AUTH_PASSWORD_VALIDATORS
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from .models import Customer, Hereglegch, HereglegchRole,Product,Manufacturer,ProdBrand,Company, HereglegchState
from django.views.generic import ListView
from .forms import NameForm, HereglegchForm
from django.views.decorators.csrf import csrf_exempt

# class CompanyListView(ListView):
#     model = Company

def home(request):
    if 'user_id' in request.session:
        h = Hereglegch.objects.get(pk=request.session['user_id'])
        return render(request,'home.html', {'user': h  })
    # if request.session.get('has_commented', False):
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
        if( p1 == p2):
            h = Hereglegch(ovog= request.POST['ovog'], ner= request.POST['ner'], role=  HereglegchRole.objects.get(pk= int(request.POST['role']))  , company=  Company.objects.get(pk=int(request.POST['company'])), password= request.POST['password'])
            h.save()
            return render(request,'home1.html' )
        else:
            h = HereglegchForm(request.POST)
            return render(request,'hereglegch.html',{'HereglegchForm': h, "errmsg": "pass tohirohguii bn"})


def hereglegchList(request):
    h = Hereglegch.objects.filter(state_id = 1).order_by('-reg_date')
    return render(request,'hereglegchList.html',{'HereglegchList': h})

@csrf_exempt
def changeState(request, hereglegch_id, state_id):
    h = Hereglegch.objects.get(pk=hereglegch_id)
    h.state = HereglegchState.objects.get(pk=state_id) 
    h.save()    
    return redirect('/reg-list')


def login(request):
    if request.method == 'GET':
        h = HereglegchForm()
        return render(request,'login.html', {'form': h})
    elif request.method == 'POST':
        h_mail = request.POST['mail']
        p = request.POST['password']
        h = Hereglegch.objects.filter(mail = h_mail)[0]
        if( h.password == p ):
            request.session['user_id'] = h.id
            return redirect('/')
        else:
            return render(request,'login.html', {'errmsg': "нэр эсвэл нууц үг тохирохгүй байна"})



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
            return HttpResponseRedirect('/get_name/')
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

def init(request):
    s1 = HereglegchState.objects.create(stateName='хүсэлт илгээсэн')
    s2 = HereglegchState.objects.create(stateName='Зөвшөөрөгдсөн')
    s3 = HereglegchState.objects.create(stateName='цуцлагдсан')
    l1 = HereglegchRole.objects.create(levelName='Түвшин1')
    l2 = HereglegchRole.objects.create(levelName='Түвшин2')
    l3 = HereglegchRole.objects.create(levelName='Түвшин3')
    c1 = Company.objects.create(comName='comp1', hayag='hayag1', phone='utas1')
    c2 = Company.objects.create(comName='comp2', hayag='hayag2', phone='utas2')
    c3 = Company.objects.create(comName='comp3', hayag='hayag3', phone='utas3')
    h1 = Hereglegch.objects.create(ovog='ovog1', ner='ner1', mail = 'user1@gmail.com',  role=l1, state=s1, company=c1, password='123' )
    h2 = Hereglegch.objects.create(ovog='ovog2', ner='ner2', mail = 'user2@gmail.com', role=l1, state=s1, company=c1, password='123')
    h3 = Hereglegch.objects.create(ovog='ovog3', ner='ner3', mail = 'user3@gmail.com', role=l1, state=s1, company=c1, password='123')
    h4 = Hereglegch.objects.create(ovog='ovog4', ner='ner4', mail = 'user4@gmail.com', role=l1, state=s1, company=c1, password='123')


    
    return render(request,'home.html')
    
