from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

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
    path('change-stateCom/<company_id>/<state_id>', views.changeStateCom),
    
    path('product',views.product,name='product'),
    path('product-list',views.productList,name='product-list'),
    path('api/product-list/<val>/<lang>',views.productListApi,name='product-list-api'),

    path('change-stateProd/<product_id>/<state_id>', views.changeStateProd),

    path('reqCom-list', views.reqComList),

    path('sum-request',views.sumRequest),

    path('customer/', views.customer),
    path('manufacturer/', views.manufacturer),
    path('prodBrand/', views.prodBrand),

    path('init', views.init),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
