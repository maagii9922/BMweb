from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('reg-user', views.hereglegch),
    path('reg-list', views.hereglegchList),
    path('change-state/<hereglegch_id>/<state_id>', views.changeState),
    path('login', views.login),
    path('thanks/', views.thanks),
    path('company/', views.company),
    path('company-list',views.companyList),
    path('product',views.product),
    path('product-list',views.productList),
    path('change-stateProd/<product_id>/<state_id>', views.changeStateProd),


    path('customer/', views.customer),
    path('manufacturer/', views.manufacturer),
    path('prodBrand/', views.prodBrand),

    path('init', views.init),
    # path('companyList/', CompanyListView.as_view()),
    # path('your-name/', views.get_name),
    # path('get_name/', views.get_name),
    path('admin/', admin.site.urls),
]
