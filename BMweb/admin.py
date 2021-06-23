from django.contrib import admin
from .models import Hereglegch,Customer,Company,HemNegj ,ProdType,Product,State,Category,Manufacturer,ProdBrand,Paiz, HereglegchRole, HereglegchState,EmHelber


# class CompanyAdmin(admin.ModelAdmin):
#     list_filter = ('comName')

# class CompanyInline(admin.TabularInline):
#     model = Company

class CompanyAdmin(admin.ModelAdmin):
    list_display= ('comName', 'hayag', 'phone')
    # inlines = [CompanyInline]    
admin.site.register(Company, CompanyAdmin)

class ProductAdmin(admin.ModelAdmin):
    filter_horizontal = ('company',)
    list_display= ('prodName', 'zCode', 'prodType','zzCode', 'price', 'hemNegj','hudNegj', 'erNershil','emHelber', 'paiz', 'uildwerlegch','uNiiluulegch','category', 'borBoloh', 'hudAwch', 'zarBoloh','state')    
admin.site.register(Product, ProductAdmin)

class ManufacturerAdmin(admin.ModelAdmin):
    list_display= ('manName', 'manPic')    
admin.site.register(Manufacturer, ManufacturerAdmin)

class ProdBrandAdmin(admin.ModelAdmin):
    list_display= ('brandName', 'brandCode','slug', 'description', 'ontslohEseh','idewhiteiEseh', 'pic', 'picBig','thumbimage', 'erembe', 'category','manufacturer')    
admin.site.register(ProdBrand, ProdBrandAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display= ('name', 'hayag','company', 'mail', 'password')    
admin.site.register(Customer, CustomerAdmin)

class PaizAdmin(admin.ModelAdmin):
    list_display= ('paizName', 'paizKey','description', 'ontslohEseh', 'picPaiz')    
admin.site.register(Paiz, PaizAdmin)

class HereglegchAdmin(admin.ModelAdmin):
    list_display= ('ovog', 'ner','mail','role','state', 'company', 'password','reg_date')    
admin.site.register(Hereglegch, HereglegchAdmin)

admin.site.register(EmHelber)
admin.site.register(HemNegj)
admin.site.register(State)
admin.site.register(Category)
admin.site.register(ProdType)
admin.site.register(HereglegchRole)
admin.site.register(HereglegchState)
# admin.site.register(Customer)
# admin.site.register(Company)
# admin.site.register(Product)
# admin.site.register(Manufacturer)
# admin.site.register(ProdBrand)
# admin.site.register(Paiz)




