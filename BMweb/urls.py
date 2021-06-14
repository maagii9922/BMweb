from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('reg-user', views.hereglegch),
    path('reg-list', views.hereglegchList),
    path('login', views.login),
    path('thanks/', views.thanks),
    path('company/', views.company),
    path('company-list',views.companyList),
    path('product',views.product),
    # path('product-list',views.productList),


    path('customer/', views.customer),
    path('manufacturer/', views.manufacturer),
    path('prodBrand/', views.prodBrand),
    # path('companyList/', CompanyListView.as_view()),
    # path('your-name/', views.get_name),
    # path('get_name/', views.get_name),
    path('admin/', admin.site.urls),
]
