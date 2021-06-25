from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login),
    path('',views.home),
    path('reg-user', views.hereglegch,name='reg-user'),
    path('reg-list', views.hereglegchList,name='reg-list'),
    path('change-state/<hereglegch_id>/<state_id>', views.changeState),
    
    path('register', views.register),

    path('thanks/', views.thanks),
    path('company/', views.company,name='company'),
    path('company-list',views.companyList,name='company-list'),
    path('product',views.product,name='product'),
    path('product-list',views.productList,name='product-list'),
    path('change-stateProd/<product_id>/<state_id>', views.changeStateProd),

    path('company-update/<company_id>',views.companyUpdate,name='company-Update'),
    # path('company-Delete/<company_id>', views.company-Delete),



    path('customer/', views.customer),
    path('manufacturer/', views.manufacturer),
    path('prodBrand/', views.prodBrand),

    path('init', views.init),
    # path('companyList/', CompanyListView.as_view()),
    # path('your-name/', views.get_name),
    # path('get_name/', views.get_name),
    path('admin/', admin.site.urls),
]
