from BMweb.settings import AUTH_PASSWORD_VALIDATORS
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .forms import HereglegchForm, CompanyForm, ProductForm,ProdType
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,HttpResponseRedirect
from .models import Customer, Hereglegch,Paiz,State, HereglegchRole,Product,Manufacturer,ProdBrand,Company,Category, HereglegchState


# class CompanyListView(ListView):

def home(request):
    if 'user_id' in request.session:
        h = Hereglegch.objects.get(pk=request.session['user_id'])
        return render(request,'home.html', {'user': h  })
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
    h = Hereglegch.objects.filter(state_id = 1).order_by('-reg_date')
    return render(request,'hereglegchList.html',{'HereglegchList': h})

@csrf_exempt
def changeState(request, hereglegch_id, state_id):
    h = Hereglegch.objects.get(pk=hereglegch_id)
    h.state = HereglegchState.objects.get(pk=state_id) 
    h.save()    
    return redirect('/reg-list')

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
        # print('asdfasjf sflj salfjsaljf slfj')
        # print(request.POST['borBoloh'])
        borb = False
        if 'borBoloh' in request.POST:
            borb = True
        huda = False
        if 'hudAwch' in request.POST:
            huda = True
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

                borBoloh= borb,
                hudAwch= huda,
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
    if request.method == 'GET':
        h = HereglegchForm()
        return render(request,'login.html', {'form': h})
    elif request.method == 'POST':
        h_mail = request.POST['mail']
        p = request.POST['password']
        h = Hereglegch.objects.filter(mail = h_mail, state_id=2)
        if ( len(h) == 0 ):
            return render(request,'login.html', {'errmsg': "нэр эсвэл нууц үг тохирохгүй байна..."})        
        if( h[0].password == p ):
            request.session['user_id'] = h[0].id
            return redirect('/')
        else:
            return render(request,'login.html', {'errmsg': "нэр эсвэл нууц үг тохирохгүй байна"})



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
    pt1 = ProdType.objects.create(typeName="prodType1")
    pt2 = ProdType.objects.create(typeName="prodType2")
    paiz1 = Paiz.objects.create(paizName="paizname1", paizKey='paizKey1', description='description1', ontslohEseh=True)
    paiz2 = Paiz.objects.create(paizName="paizname2", paizKey='paizKey2', description='description2', ontslohEseh=True)
    cat1 = Category.objects.create(catName="catName1")
    cat2 = Category.objects.create(catName="catName2")
    cat3 = Category.objects.create(catName="catName3")
    state1 = State.objects.create(stateName="stateName1")
    state2 = State.objects.create(stateName="stateName2")
    state3 = State.objects.create(stateName="stateName3")
    prod1 = Product.objects.create(prodName="prodName1", zCode=123, prodType=pt1, zzCode=123, price=123, hemNegj=123, hudNegj=123, company=c1, erNershil= 'erNershil1', emHelber="emHelber1", paiz=paiz1, uildwerlegch="uildwerlegch1", category=cat1, borBoloh=True, hudAwch=True, state=state1)
    # prod1 = Product.objects.create(prodName="prodName1", zCode="zCode1", prodType=pt1, zzCode=123, price=123, hemNegj=123, hudNegj=123, company=c1, erNershil= 'erNershil1', emHelber="emHelber1", paiz=paiz1, uildwerlegch="uildwerlegch1", category=cat1, borBoloh=True, hudAwch=True, state=state1)




    return render(request,'home.html')
    
