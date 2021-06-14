from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('reg-user', views.hereglegch),
    path('reg-list', views.hereglegchList),
    path('change-state/<hereglegch_id>/<state_id>', views.changeState),
    path('login', views.login),
    path('your-name/', views.get_name),
    path('thanks/', views.thanks),
    
    path('customer/', views.customer),
    path('get_name/', views.get_name),
    path('manufacturer/', views.manufacturer),
    path('prodBrand/', views.prodBrand),

    path('init', views.init),
    # path('companyList/', CompanyListView.as_view()),
    path('admin/', admin.site.urls),
]
