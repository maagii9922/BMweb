from BMweb.settings import AUTH_PASSWORD_VALIDATORS, DATABASES
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .forms import HereglegchForm, CompanyForm, ProductForm,ProdType
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,HttpResponseRedirect, request, response, JsonResponse
from .models import Customer, EmHelber, HemNegj, Hereglegch, Hutlult,Paiz, PosCategory,State,Niiluulegch, HereglegchRole,Product,Manufacturer,ProdBrand,Company,Category, HereglegchState
from django.contrib.auth.models import User
import base64
from django.core.files.storage import FileSystemStorage
from django.core import serializers
from django.core.paginator import Paginator

import json
import random
import urllib.request
import odoorpc
HOST = '10.0.0.178'
PORT = 8069
DB = 'test-training​'


USER = 'admin_cos'
PASS = 'M*on8aalj'
import json
import random
import urllib.request



def odoo_rpc():
    odoo = odoorpc.ODOO(HOST, port=PORT)

    connection = odoo.login('test-training', 'admin_cos', 'M*on8aalj')    
    # user = odoo.env.user
    # return connection
    return odoo


def get_user_data():
    odoo = odoo_rpc()
    user = odoo.env.user
    user_data = odoo.env['res.users'].search_read([('id', '=', [user.id])])
    # print("user_data", user_data)
    # print("user_data", user_data[0])
    print("user_data", user_data[0]['id'])
    return user_data
    

# ,('default_code')('barcode')
def get_product_data():
    odoo = odoo_rpc()
    product_ids = odoo.env['product.product'].search_read([("id", "=", 3)])
    # print('product', product_ids[0])
    for key , v in product_ids[0].items():
        print(key, ' ->', v) 
    # for product_id in product_ids:
    #     product_name = product_id["name"]
    #     print("product_name", product_name)
    return 'hello' 

def get_product_name(prodName):
    odoo = odoo_rpc()
    product_ids = odoo.env['product.product'].search_read([("name", "=", prodName)])
    names = []
    for v in product_ids:
       names.append(v['name'])
    print(names)
    return names

def get_product_category():
    odoo = odoo_rpc()
    product_ids = odoo.env['product.category'].search([])   #.search_read([("id", "=", 1)])
    print(product_ids[0])
    # print(odoo.db.list())
    return 678

def odoo(request):
    pass
    odoo_rpc()
    # get_user_data()
    # get_product_name('Хөнгөлөлт')
    get_product_category()
    return HttpResponse('asfsdf')


def login(request):
    if request.method == 'GET':
        h = HereglegchForm()
        return render(request,'login.html', {'form': h})
    elif request.method == 'POST':
        h_mail = request.POST['mail']
        p = request.POST['password']
        h = Hereglegch.objects.filter(mail = h_mail, state_id=2)
        if ( len(h) == 0 ):
            return render(request,'login.html', {'errmsg': "Нэвтрэх нэр эсвэл нууц үг тохирохгүй байна..."})        
        if( h[0].password == p ):
            request.session['user_id'] = h[0].id
            return redirect('/')
        else:
            return render(request,'login.html', {'errmsg': "Нэвтрэх нэр эсвэл нууц үг тохирохгүй байна"})
    
def home(request):    
    if 'user_id' in request.session:
        h = Hereglegch.objects.get(pk=request.session['user_id'])
        print(h.role_id)
        if h.role_id == 1:
            return redirect('/product-list')
        elif h.role_id == 2:
            return redirect('/company-list')
        elif h.role_id == 3:
            return redirect('/reqCom-list')
        elif h.role_id == 4:
            return redirect('/sum-request')
    else:
        return redirect('/login')        
        
    
      
    # if 'user_id' in request.session:
    #     h = Hereglegch.objects.get(pk=request.session['user_id'])
    #     return render(request,'home.html', {'user': h })
        
    # return render(request,'home.html')

def hereglegch(request):
    if request.method == 'GET':
        form = HereglegchForm()
        return render(request,'hereglegch.html', {'HereglegchForm': HereglegchForm})
    elif request.method == 'POST':
        p1 = request.POST['password']
        p2 = request.POST['password1']
        if(p1 == p2):
            h = Hereglegch(ovog= request.POST['ovog'], ner= request.POST['ner'], mail= request.POST['mail'], role=  HereglegchRole.objects.get(pk= int(request.POST['role']))  ,state=  HereglegchState.objects.get(pk= int(request.POST['state']))  , company=  Company.objects.get(pk=int(request.POST['company'])), password= request.POST['password'],reg_date= request.POST['reg_date'])
            h.save()
            return render(request,'home1.html' )
        else:
            h = HereglegchForm(request.POST)
            return render(request,'hereglegch.html',{'HereglegchForm': h, "errmsg": "Нууц үг тохирохгүй байна."})

def hereglegchList(request):
    if 'user_id' in request.session:
        h = Hereglegch.objects.get(pk=request.session['user_id'])
        return render(request,'hereglegchList.html', {'user': h })
    h = Hereglegch.objects.filter(state_id = 1).order_by('-reg_date')
    return render(request,'hereglegchList.html',{'HereglegchList': h})

@csrf_exempt
def changeState(request, hereglegch_id, state_id):
    h = Hereglegch.objects.get(pk=hereglegch_id)
    h.state = HereglegchState.objects.get(pk=state_id) 
    h.save()    
    return redirect('/reg-list')

def company(request):
    if 'user_id' in request.session:
        h = Hereglegch.objects.get(pk=request.session['user_id'])
        if request.method == 'GET':
            if 'edit' in request.GET :
                p = Company.objects.get(pk=request.GET['edit'])
                # print(p)  
                return render(request,'company.html',{'user': h, "edit": request.GET['edit'],  "data": p} )
            elif 'del' in request.GET :
                p = Company.objects.get(pk=request.GET['del'])
                p.delete()
                return redirect('/')
            else:
                return render(request,'company.html', {'user': h})
       
        elif request.method == 'POST':
            if 'edit' in request.POST :
                p = Company.objects.get(pk=request.POST['edit'])
                p.comName= request.POST['comName']
                p.hayag= request.POST['hayag']
                p.phone = request.POST['phone']
                p.thumbimage = request.POST['thumbimage']
                # p.description = request.POST['description']
                # p.comState = request.POST['comState']
                p.save()
                return redirect('/')
            else:
                if Company.objects.filter(comName= request.POST['comName']):
                    errmsg = "Компаний нэр давхардлаа"       
                    return render(request,'company.html', {'user': h, "errmsg": errmsg})                               
                p = Company(comName= request.POST['comName'], hayag= request.POST['hayag'], phone= request.POST['phone'],thumbimage = request.POST['thumbimage'],comState = State.objects.get(pk= 1),reg_user=request.session['user_id'])
                p.save()
                return redirect('/', {'user': h})            
            
def companyList(request):
    if 'user_id' in request.session:
        p = Company.objects.filter(reg_user=request.session['user_id']).order_by('comState')
        # print(p)
        # p = Company.objects.filter(comState_id=1).order_by('comState')

        # h = Hereglegch.objects.filter(pk=request.session['user_id'])
        # print(h)
        # if h.role_id == 2:
        #     p=Company.objects.filter(reg_user=request.session['user_id']).order_by('comState')
        # elif h.role_id == 3:
        #     p=Company.objects.filter(comState_id=1).order_by('comState')

        size = 25
        if 'size' in request.GET:
            size = request.GET['size']
        pc = Paginator(p, size)
        page_num = 1
        
        if 'page' in request.GET:
            page_num = int(request.GET['page'])
            print('page')
            print(page_num)
        page=pc.page(page_num)
        h = Hereglegch.objects.get(pk=request.session['user_id'])
        return render(request,'companyList.html', {'user': h, 'companyList': page.object_list, 'size':size, 'count':pc.count, 'page_count': pc.num_pages, 'page_range':pc.page_range, 'page_num':page_num, 'has_next':page.has_next(), 'has_previous': page.has_previous(), 'start_index':page.start_index() })
    else: 
        return redirect('/login')  

@csrf_exempt
def changeStateCom(request, company_id, state_id, desc=''):
    h = Company.objects.get(pk=company_id)
    h.comState = State.objects.get(pk=state_id) 
    h.save()    
    return redirect('/reqCom-list')

def product(request):
    # r = HereglegchRole(levelname = 'Бараа шинээр бүртгэх хүсэлт илгээх')
    # r.save()
    if 'user_id' in request.session:
        h = Hereglegch.objects.get(pk=request.session['user_id'])
        b = ProdBrand.objects.all()
        t = ProdType.objects.all()
        eh = EmHelber.objects.all()
        comp = Company.objects.all()
        # cat = Category.objects.filter(parent__isnull=True)
        cat = Category.objects.all()
        hemNegj = HemNegj.objects.all()
        uildwerlegch = Manufacturer.objects.all()
        uNiiluulegch = Niiluulegch.objects.all()
        paiz = Paiz.objects.all()
        posCat = PosCategory.objects.all()
        hutlult = Hutlult.objects.all()
        print(posCat)
        if request.method == 'GET':
            if 'edit' in request.GET :
                p = Product.objects.get(pk=request.GET['edit'])
                cc = p.company.all().values_list('id', flat=True)
                kk = []
                for id in cc:
                    kk.append(str(id))
                # print(p)    
                # print(kk)  
                return render(request,'product.html',{'user': h, "edit": request.GET['edit'],  "data": p, 'selected_company': kk,'brand': b, 'type': t, 'emHelber': eh, 'cat': cat, 'comp': comp, 'hemNegj': hemNegj, 'uildwerlegch':uildwerlegch, 'paiz': paiz, 'uNiiluulegch': uNiiluulegch,'posCat':posCat,'hutlult':hutlult} )
            elif 'del' in request.GET :
                p = Product.objects.get(pk=request.GET['del'])
                p.delete()
                return redirect('/')
            else:
                return render(request,'product.html', {'user': h, 'brand': b, 'type': t, 'emHelber': eh, 'cat': cat, 'comp': comp, 'hemNegj': hemNegj, 'uildwerlegch':uildwerlegch, 'paiz': paiz, 'uNiiluulegch': uNiiluulegch, 'posCat':posCat,'hutlult':hutlult})
        elif request.method == 'POST':            
            print(request.POST)
            if 'edit' in request.POST :
                p = Product.objects.get(pk=request.POST['edit'])
                print(p)
                print(ProdBrand.objects.get(pk= request.POST['brand_id']))
                p.prodName= request.POST['prodName']
                p.prodName_en= request.POST['prodName_en']
                p.brand = ProdBrand.objects.get(pk= request.POST['brand_id'])
                p.zCode= request.POST['zCode']
                p.prodType=  ProdType.objects.get(pk= int(request.POST['prodType_id']))
                        # zzCode= request.POST['zzCode'],
                p.price= request.POST['price']
                p.hemNegj= HemNegj.objects.get(pk= int(request.POST['hemNegj_id']))
                p.hudNegj= HemNegj.objects.get(pk= int(request.POST['hudNegj_id']))
                # p.hudNegj= request.POST['hudNegj']
                p.category=  Category.objects.get(pk= int(request.POST['category_id']))
                p.erNershil= request.POST['erNershil']
                p.emHelber= EmHelber.objects.get(pk= int(request.POST['emHelber_id']))
                p.paiz=  Paiz.objects.get(pk= int(request.POST['paiz_id']))
                p.uildwerlegch= Manufacturer.objects.get(pk= int(request.POST['uildwerlegch_id']))
                p.uNiiluulegch= Niiluulegch.objects.get(pk= int(request.POST['uNiiluulegch_id']))
                        # uNiiluulegch= request.POST['uNiiluulegch'],
                        # prodBrand=  ProdBrand.objects.get(pk= int(request.POST['prodBrand'])),
                borb = False
                if 'borBoloh' in request.POST:
                    borb = True
                p.borBoloh= borb
                huda = False
                if 'hudAwch' in request.POST:
                    huda = True
                p.hudAwch= huda
                zarb = False
                if 'zarBoloh' in request.POST:
                    zarb = True
                p.zarBoloh= zarb
                huda = False
                if 'pos' in request.POST:
                    huda = True
                p.pos= huda
                        # hudAwch= huda,
                        # zarBoloh= zarb,
                # p.state=  State.objects.get(pk= 1),
                p.posCat=  PosCategory.objects.get(pk= int(request.POST['posCat_id']))
                p.hutlult=  Hutlult.objects.get(pk= int(request.POST['hutlult_id']))
                p.thumbimage = request.POST['thumbimage']
                p.save()
                p.company.clear()
                company=  Company.objects.filter(pk__in = request.POST.getlist('selected_company'))
                # print(company)
                p.company.add(*company)
                return redirect('/')
            else:
                # print(request.FILES)
                # upFile = request.FILES['thumbimage']
                # data = upFile.read()
                # encoded = base64.b64encode(data)
                # mime = "image/jpeg"
                # mime = mime + ";" if mime else ";"
                # f = {"upFile": "data:%sbase64,%s" % (mime, encoded)}

                # myfile = request.FILES['thumbimage']
                # fs = FileSystemStorage()
                # filename = fs.save(myfile.name, myfile)
                # uploaded_file_url = fs.url(filename)
                # return render(request, 'index.html', {'uploaded_file_url': uploaded_file_url })


                if Product.objects.filter(prodName = request.POST['prodName']):
                    errmsg = "Барааны монгол нэр давхардлаа"         #Company.objects.filter(pk__in = request.POST.getlist('selected_company'))
                    return render(request,'product.html', {'user': h, "errmsg": errmsg, "data": request.POST, "selected_company": request.POST.getlist('selected_company') , "company_id": request.POST['company_id'], 'brand': b, 'type': t, 'emHelber': eh, 'cat': cat, 'comp': comp, 'hemNegj': hemNegj, 'uildwerlegch':uildwerlegch, 'paiz': paiz, 'uNiiluulegch': uNiiluulegch})
                if Product.objects.filter(prodName_en = request.POST['prodName_en']):
                    errmsg = "Барааны англи нэр давхардлаа"
                    return render(request,'product.html', {'user': h, "errmsg": errmsg, "data": request.POST, "selected_company": request.POST.getlist('selected_company'), "company_id": request.POST['company_id'], 'brand': b, 'type': t, 'emHelber': eh, 'cat': cat, 'comp': comp, 'hemNegj': hemNegj, 'uildwerlegch':uildwerlegch, 'paiz': paiz, 'uNiiluulegch': uNiiluulegch})
                if Product.objects.filter(zCode = request.POST['zCode']):
                    errmsg = "Зураасан код давхардлаа"
                    return render(request,'product.html', {'user': h, "errmsg": errmsg, "data": request.POST, "selected_company": request.POST.getlist('selected_company'), "company_id": request.POST['company_id'], 'brand': b, 'type': t, 'emHelber': eh, 'cat': cat, 'comp': comp, 'hemNegj': hemNegj, 'uildwerlegch':uildwerlegch, 'paiz': paiz, 'uNiiluulegch': uNiiluulegch})
                borb = False
                if 'borBoloh' in request.POST:
                    borb = True
                huda = False
                if 'hudAwch' in request.POST:
                    huda = True
                zarb = False
                if 'zarBoloh' in request.POST:
                    zarb = True
                pos = False
                if 'pos' in request.POST:
                    pos = True
                # h = ProductForm(request.POST, request.FILES)
                data = request.POST['prodName']
                # if data :
                #     get_user_data(data)

                    
                h = Product(
                        prodName= request.POST['prodName'],
                        prodName_en= request.POST['prodName_en'],
                        brand = ProdBrand.objects.get(pk= request.POST['brand_id']),
                        zCode= request.POST['zCode'],
                        prodType=  ProdType.objects.get(pk= int(request.POST['prodType_id'])),
                        # zzCode= request.POST['zzCode'],
                        price= request.POST['price'],
                        hemNegj= HemNegj.objects.get(pk= int(request.POST['hemNegj_id'])),
                        hudNegj= HemNegj.objects.get(pk= int(request.POST['hudNegj_id'])),  
                        category=  Category.objects.get(pk= int(request.POST['category_id'])),
                        erNershil= request.POST['erNershil'],
                        emHelber= EmHelber.objects.get(pk= int(request.POST['emHelber_id'])),
                        paiz=  Paiz.objects.get(pk= int(request.POST['paiz_id'])),
                        uildwerlegch= Manufacturer.objects.get(pk= int(request.POST['uildwerlegch_id'])),
                        uNiiluulegch= Niiluulegch.objects.get(pk= int(request.POST['uNiiluulegch_id'])),
                        # uNiiluulegch= request.POST['uNiiluulegch'],
                        # prodBrand=  ProdBrand.objects.get(pk= int(request.POST['prodBrand'])),                        
                        borBoloh= borb,
                        hudAwch= huda,
                        zarBoloh= zarb,
                        pos= pos,
                        posCat = PosCategory.objects.get(pk= int(request.POST['posCat_id'])),
                        thumbimage = request.POST['thumbimage'],
                        hutlult = Hutlult.objects.get(pk= int(request.POST['hutlult_id'])),
                        state=  State.objects.get(pk= 1),
                        )
                
                h.save()
                company=  Company.objects.filter(pk__in = request.POST.getlist('selected_company'))
                
                # print(company)
                h.company.add(*company)                
                # return render(request,'product.html',{'user': h,  "data": request.POST, 'brand': b, 'type': t, 'emHelber': eh, 'cat': cat, 'comp': comp, 'hemNegj': hemNegj, 'uildwerlegch':uildwerlegch} )
                return redirect('/')

def productListApi(request, val, lang): 
    print(val)
    # if lang=='mn':
    #     plist = Product.objects.filter(prodName__startswith = val).only("prodName")
    # elif lang=='eng':
    #     plist = Product.objects.filter(prodName_en__startswith = val).only("prodName_en")
    # print(plist)
    # data = []
    # for i, p in enumerate(plist):
    #     if lang=='mn':
    #         data.append(p.prodName)
    #     elif lang=='eng':
    #         data.append(p.prodName_en)
    # print (data)
    data = get_product_name(val)
    return JsonResponse({'data': data})

def productList(request):    
    if 'user_id' in request.session:
        p = Product.objects.all().order_by('state')
        size = 25
        if 'size' in request.GET:
            size = request.GET['size']
        pc = Paginator(p, size)
        page_num = 1
        
        if 'page' in request.GET:
            page_num = int(request.GET['page'])
            print('page')
            print(page_num)
        page=pc.page(page_num)
        h = Hereglegch.objects.get(pk=request.session['user_id'])
        
        return render(request,'productList.html', {'user': h, 'productList': page.object_list, 'size':size, 'count':pc.count, 'page_count': pc.num_pages, 'page_range':pc.page_range, 'page_num':page_num, 'has_next':page.has_next(), 'has_previous': page.has_previous(), 'start_index':page.start_index() })
    else: 
        return redirect('/login')  

@csrf_exempt
def changeStateProd(request, product_id, state_id, desc=''):
    print(desc)
    h = Product.objects.get(pk=product_id)
    h.state = State.objects.get(pk=state_id) 
    h.save()    
    return redirect('/reqCom-list')

def register(request):
    return render(request,'register.html')

def customer(request):
    c = Customer.objects.all()
    # print(h)
    return render(request,'login.html',{'customer':c})

def reqComList(request):
    if 'user_id' in request.session:
        c = Company.objects.all()
        p = Product.objects.all()
        h = Hereglegch.objects.get(pk=request.session['user_id'])
        # size = 25
        # if 'size' in request.GET:
        #     size = request.GET['size']
        # pc = Paginator(p, size)
        # page_num = 1
        
        # if 'page' in request.GET:
        #     page_num = int(request.GET['page'])
        #     print('page')
        #     print(page_num)
        # page=pc.page(page_num)
        # h = Hereglegch.objects.get(pk=request.session['user_id'])

        return render(request,'requestList.html', {'user': h, 'companyList': c, 'productList': p})
        # return render(request,'requestList.html', {'user': h, 'productList': page.object_list, 'companyList': page.object_list, 'size':size, 'count':pc.count, 'page_count': pc.num_pages, 'page_range':pc.page_range, 'page_num':page_num, 'has_next':page.has_next(), 'has_previous': page.has_previous(), 'start_index':page.start_index() })
    else: 
        return redirect('/login')  

def sumRequest(request):
    if 'user_id' in request.session:
        c = Company.objects.all()
        p = Product.objects.all()
        h = Hereglegch.objects.get(pk=request.session['user_id'])
        return render(request,'sumRequest.html', {'user': h, 'companyList': c, 'productList': p})
    else: 
        return redirect('/login') 

def thanks(request):
    return HttpResponse('thanks')

def manufacturer(request):
    m = Manufacturer.objects.all()
    return render(request,'test.html', {'manufacturer': m})

def prodBrand(request):
    b = ProdBrand.objects.all()
    return render(request,'test.html', {'prodBrand': b})

def init(request):
    # admin = User.objects.create_user(value['USERNAME'], value['EMAIL'], value['PASSWORD'])
    # admin = User.objects.create_superuser('admin1', 'aa@gmail.com', '123')
    # admin.is_staff = True
    # admin.save()
    s1 = HereglegchState.objects.create(stateName='Хүсэлт илгээсэн')
    s2 = HereglegchState.objects.create(stateName='Зөвшөөрөгдсөн')
    s3 = HereglegchState.objects.create(stateName='Цуцлагдсан')
    l1 = HereglegchRole.objects.create(levelName='Бараа шинээр бүртгэх хүсэлт илгээх')
    l2 = HereglegchRole.objects.create(levelName='Харилцагч шинээр бүртгэх хүсэлт илгээх')
    l3 = HereglegchRole.objects.create(levelName='Бараа болон харилцагч шинээр бүртгэх хүсэлт хянаад зөвшөөрөх')
    l4 = HereglegchRole.objects.create(levelName='Дата бүртгэлийн ажилтан')
    pt1 = ProdType.objects.create(typeName="Үйлчилгээ")
    pt2 = ProdType.objects.create(typeName="Үлдэгдэл тооцох")
    paiz1 = Paiz.objects.create(paizName="emonos", paizKey='paizKey1', description='description1', ontslohEseh=True)
    paiz2 = Paiz.objects.create(paizName="Ундрам хан хангай ХХК", paizKey='paizKey2', description='description2', ontslohEseh=True)
    cat1 = Category.objects.create(catName="ЭМ")
    cat2 = Category.objects.create(catName="ЭМН.ТУСЛАМЖ")
    cat3 = Category.objects.create(catName="ВИТАМИН", parent=2)
    cat4 = Category.objects.create(catName="Эмнэлгийн хэрэгсэл")
    cat5 = Category.objects.create(catName="Гэмтлийн үеийн хэрэгсэл", parent=4)
    cat6 = Category.objects.create(catName="Сойлт, бэхэлгээ, чиг", parent=5)
    # cus1 = Customer.objects.create(name='comp1', hayag='hayag1', company='utas1',mail='mail',password='123')
    # cus2 = Customer.objects.create(name='comp1', hayag='hayag1', company='utas1',mail='mail',password='123')
    # cus3 = Customer.objects.create(name='comp1', hayag='hayag1', company='utas1',mail='mail',password='123')
    
    state1 = State.objects.create(stateName="Илгээсэн")
    state2 = State.objects.create(stateName="Цуцалсан")
    state3 = State.objects.create(stateName="Батлагдсан")
    posCat1 = PosCategory.objects.create(posCatName="posCatName1")
    posCat2 = PosCategory.objects.create(posCatName="posCatName2")
    c1 = Company.objects.create(comName='emonos', hayag='hayag1', phone='utas1',comState=state1,description="sdsddf",reg_user=2)
    c2 = Company.objects.create(comName='Ундрам хан хангай ХХК', hayag='hayag2', phone='utas2',comState=state2,description="cdhgfh",reg_user=6)
    c3 = Company.objects.create(comName='МУБ', hayag='hayag3', phone='utas3',comState=state3,description="cdhgfh",reg_user=2)
    c4 = Company.objects.create(comName='emonos2', hayag='hayag1', phone='utas1',comState=state1,description="sdsddf",reg_user=2)
    c5 = Company.objects.create(comName='Ундрам хан хангай ХХК2', hayag='hayag2', phone='utas2',comState=state2,description="cdhgfh",reg_user=6)
    c6 = Company.objects.create(comName='МУБ2', hayag='hayag3', phone='utas3',comState=state3,description="cdhgfh",reg_user=2)
    h1 = Hereglegch.objects.create(ovog='Батаа', ner='Мандах', mail = 'user1@gmail.com', role=l1, state=s2, company=c1, password='123')
    h2 = Hereglegch.objects.create(ovog='Сараа', ner='Батаа', mail = 'user2@gmail.com', role=l2, state=s2, company=c1, password='123')
    h3 = Hereglegch.objects.create(ovog='Мандах', ner='Дорж', mail = 'user3@gmail.com', role=l3, state=s2, company=c1, password='123')
    h4 = Hereglegch.objects.create(ovog='Дорж', ner='Сараа', mail = 'user4@gmail.com', role=l4, state=s2, company=c1, password='123')
    h5 = Hereglegch.objects.create(ovog='Батаа', ner='Мандах2', mail = 'user5@gmail.com', role=l1, state=s2, company=c1, password='123')
    h6 = Hereglegch.objects.create(ovog='Сараа', ner='Батаа2', mail = 'user6@gmail.com', role=l2, state=s2, company=c1, password='123')
    h7 = Hereglegch.objects.create(ovog='Мандах', ner='Дорж2', mail = 'user7@gmail.com', role=l3, state=s2, company=c1, password='123')
    h8 = Hereglegch.objects.create(ovog='Дорж', ner='Сараа2', mail = 'user8@gmail.com', role=l4, state=s2, company=c1, password='123')
    em1 = EmHelber.objects.create(emHelberName="Тун")
    em2 = EmHelber.objects.create(emHelberName="Капсул")
    hut1 = Hutlult.objects.create(hutlultName="Цувралаар")
    hut2 = Hutlult.objects.create(hutlultName="Үл давтагдах")
    hut3 = Hutlult.objects.create(hutlultName="Мөшгөхгүй")
    hemNegj1 = HemNegj.objects.create(hemNegjName="гр")
    hemNegj2 = HemNegj.objects.create(hemNegjName="мл")
    uildver1 = Manufacturer.objects.create(manName="Япон")
    uildver2 = Manufacturer.objects.create(manName="Америк")
    uildver3 = Manufacturer.objects.create(manName="Орос")
    uildver4 = Manufacturer.objects.create(manName="Хятад")
    niil1 = Niiluulegch.objects.create(niiName="Буман Ай Ти")
    niil2 = Niiluulegch.objects.create(niiName="МУБ")
    niil3 = Niiluulegch.objects.create(niiName="Ундрам хан хангай ХХК")
    niil4 = Niiluulegch.objects.create(niiName="emonos")
    brand1 = ProdBrand.objects.create(brandName="Pigeon", brandCode="brandCode1", description="description1", ontslohEseh=False, idewhiteiEseh=True)
    brand2 = ProdBrand.objects.create(brandName="Friso", brandCode="brandCode2", description="description2", ontslohEseh=False, idewhiteiEseh=True)
    prod1 = Product.objects.create(prodName="Сүү", prodName_en="Friso", brand=brand1, zCode=123, prodType=pt1, hutlult=hut1, zzCode=123, price=123, hemNegj=hemNegj1, hudNegj=hemNegj2, erNershil= 'erNershil1', emHelber=em1, paiz=paiz1, uildwerlegch=uildver1,uNiiluulegch=niil1, category=cat1, borBoloh=True, hudAwch=True, zarBoloh=True,pos=True,state=state1, posCat=posCat1,description="cdhgfh")
    prod1.company.add(c1)
    prod1.company.add(c2)
    prod1.company.add(c3)
    prod2 = Product.objects.create(prodName="Угж", prodName_en="Pigeon", brand=brand2, zCode=123, prodType=pt1, hutlult=hut2,  zzCode=123, price=123, hemNegj=hemNegj1, hudNegj=hemNegj2, erNershil= 'erNershil2', emHelber=em1, paiz=paiz1, uildwerlegch=uildver1,uNiiluulegch=niil2, category=cat2, borBoloh=True, hudAwch=True, zarBoloh=True,pos=True,state=state1, posCat=posCat2,description="cdhgfh")
    prod2.company.add(c3)
    prod2.company.add(c2)
    prod2.company.add(c1)




    return redirect('/')
    
