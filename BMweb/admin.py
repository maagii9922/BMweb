from django.contrib import admin
from .models import Hereglegch,Customer,Company,ProdType,Product,State,Category,Manufacturer,ProdBrand,Paiz, HereglegchRole


# class CompanyAdmin(admin.ModelAdmin):
#     list_filter = ('comName')

admin.site.register(Hereglegch)
admin.site.register(Customer)
admin.site.register(Company)
admin.site.register(ProdType)
admin.site.register(Product)
admin.site.register(State)
admin.site.register(Category)
admin.site.register(Manufacturer)
admin.site.register(ProdBrand)
admin.site.register(Paiz)
admin.site.register(HereglegchRole)




