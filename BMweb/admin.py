from django.contrib import admin
from .models import Hereglegch,Customer,Company,ProdType,Product,State,Category,Manufacturer,ProdBrand,Paiz, HereglegchRole, HereglegchState


# class CompanyAdmin(admin.ModelAdmin):
#     list_filter = ('comName')

# class CompanyInline(admin.TabularInline):
#     model = Company

class CompanyAdmin(admin.ModelAdmin):
    list_display= ('comName', 'hayag', 'phone')
    # inlines = [CompanyInline]    
admin.site.register(Company, CompanyAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display= ('prodName', 'zCode', 'prodType','zzCode', 'price', 'hemNegj','hudNegj', 'company', 'erNershil','emHelber', 'paiz', 'uildwerlegch', 'uNiiluulegch','category', 'borBoloh', 'hudAwch','state')    
admin.site.register(Product, ProductAdmin)

class ManufacturerAdmin(admin.ModelAdmin):
    list_display= ('manName', 'manPic')    
admin.site.register(Manufacturer, ManufacturerAdmin)

class ProdBrandAdmin(admin.ModelAdmin):
    list_display= ('brandName', 'brandCode','slug', 'description', 'ontslohEseh','idewhiteiEseh', 'pic', 'picBig','thumbimage', 'erembe', 'category','manufacturer')    
admin.site.register(ProdBrand, ProdBrandAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display= ('name', 'code','company', 'mail', 'password')    
admin.site.register(Customer, CustomerAdmin)

class PaizAdmin(admin.ModelAdmin):
    list_display= ('paizName', 'paizKey','description', 'ontslohEseh', 'picPaiz')    
admin.site.register(Paiz, PaizAdmin)

class HereglegchAdmin(admin.ModelAdmin):
    list_display= ('ovog', 'ner','role', 'company', 'password')    
admin.site.register(Hereglegch, HereglegchAdmin)


admin.site.register(State)
admin.site.register(Category)
admin.site.register(ProdType)
admin.site.register(HereglegchRole)
# admin.site.register(Hereglegch)
# admin.site.register(Customer)
# admin.site.register(Company)
# admin.site.register(Product)
# admin.site.register(Manufacturer)
# admin.site.register(ProdBrand)
# admin.site.register(Paiz)




