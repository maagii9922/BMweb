from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.utils.translation import ugettext_lazy as _

from datetime import datetime   


class Company(models.Model):
    comName = models.CharField(max_length=50, verbose_name=_("Компаний нэр"))
    hayag = models.CharField(max_length=150, verbose_name=_("Компаний хаяг"))
    phone = models.CharField(max_length=30, verbose_name=_("Компаний утас"))

    class Meta:
        verbose_name = _("Компани")
        verbose_name_plural = _("Компани")
    
    def __str__(self):
        #  return self.comName
        return '%s %s %s' % (self.comName, self.hayag, self.phone)

class HereglegchRole(models.Model):
    levelName = models.CharField(max_length=300, verbose_name=_("Эрхийн түвшин"))
    class Meta:
        verbose_name = _("Эрхийн түвшин")
        verbose_name_plural = _("Эрхийн түвшин")

    def __str__(self):
        return self.levelName

class HereglegchState(models.Model):
    stateName = models.CharField(max_length=300, verbose_name=_("Хэрэглэгч төлөв"))
    class Meta:
        verbose_name = _("Хэрэглэгч төлөв")
        verbose_name_plural = _("Хэрэглэгч төлөв")
    def __str__(self):
        return self.stateName
class Hereglegch(models.Model):
    ovog=models.CharField(max_length=30, verbose_name=_("Хэрэглэгчийн  овог"))
    ner=models.CharField(max_length=30, verbose_name=_("Хэрэглэгчийн нэр"))
    mail = models.CharField(max_length=30, verbose_name=_("мейл хаяг"))
    role = models.ForeignKey(HereglegchRole, on_delete=CASCADE )
    state = models.ForeignKey(HereglegchState, on_delete=CASCADE )
    company = models.ForeignKey(Company, on_delete=CASCADE )
    password  = models.CharField(max_length=30, verbose_name=_("Хэрэглэгчийн нууц үг"))
    reg_date = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = _("Хэрэглэгч")
        verbose_name_plural = _("Хэрэглэгч")

    def __str__(self):
        return '%s %s %s' % (self.ovog, self.ner, self.role)


class Category(models.Model):
    catName = models.CharField(max_length=50, verbose_name=_("Ангилалын нэр"))

    class Meta:
        verbose_name = _("Ангилал")
        verbose_name_plural = _("Ангилал")

    def __str__(self):
        return self.catName

class Manufacturer(models.Model):
    manName = models.CharField(max_length=50,verbose_name=_("Үйлдвэрлэгчийн нэр"))
    manPic = models.ImageField(upload_to="media/manufacturer/", verbose_name=_("Зураг"))

    class Meta:
        verbose_name = ("Үйлдвэрлэгч")
        verbose_name_plural = ("Үйлдвэрлэгч")

    def __str__(self):
        return self.manName

class ProdBrand(models.Model):
    brandName = models.CharField(max_length=50, verbose_name=_("Бренд нэр"))
    brandCode = models.CharField(max_length=50,  verbose_name=_("Бренд код"))
    slug = models.SlugField()
    description = models.TextField(verbose_name=_("Тайлбар"))
    # ontslohEseh = models.IntegerField(null=True, blank=True, verbose_name=_("Онцлох эсэх"))
    ontslohEseh = models.BooleanField(verbose_name=_("Онцлох эсэх"))
    idewhiteiEseh = models.BooleanField(verbose_name=_("Идэвхитэй эсэх"))
    pic = models.ImageField(upload_to="media/brand/", verbose_name=_("Зураг"))
    picBig = models.ImageField(upload_to="media/brand/", verbose_name=_("Том зураг"))
    thumbimage = models.ImageField(upload_to="media/brandthumb/", verbose_name=_("Зураг"))
    erembe = models.IntegerField(null=True, blank=True, verbose_name=_("Эрэмбэ"))
    category = models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name=_("Ангилал"))
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE,verbose_name=_("Үйлдвэрлэгч"))

    class Meta:
        verbose_name = _("Бүтээгдэхүүний бренд")
        verbose_name_plural = _("Бүтээгдэхүүний бренд")

    def __str__(self):
        return self.brandName+" "+str(self.manufacturer)

class Customer(models.Model):
    name = models.CharField(max_length=30, verbose_name=_("Харилцагчийн нэр"))
    code = models.CharField(max_length=30, verbose_name=_("Харилцагчийн код"))
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    mail = models.CharField(max_length=50, verbose_name=_("Компаний майл"))
    password = models.CharField(max_length=50, verbose_name=_("Майлын нууц үг"))

    class Meta:
        verbose_name = _("Харилцагч")
        verbose_name_plural = _("Харилцагч")

    def __str__(self):
        return self.name

class ProdType(models.Model):
    typeName = models.CharField(max_length=50, verbose_name=_("Төрлийн нэр"))

    class Meta:
        verbose_name = _("Барааны төрөл")
        verbose_name_plural = _("Барааны төрөл")

    def __str__(self):
        return self.typeName

class State(models.Model):
    stateName = models.CharField(max_length=50, verbose_name=_("Төлөвийн нэр"))

    class Meta:
        verbose_name = _("Барааны төлөв")
        verbose_name_plural = _("Барааны төлөв")

    def __str__(self):
        return self.stateName
         

class Paiz(models.Model):
    paizName = models.CharField(max_length=50, verbose_name=_("Пайзын нэр"))
    paizKey = models.CharField(max_length=50, verbose_name=_("Пайзын түлхүүр"))
    description = models.TextField(verbose_name=_("Тайлбар"))
    ontslohEseh = models.BooleanField(verbose_name=_("Онцлох эсэх"))
    picPaiz = models.ImageField(upload_to="media/paiz/", verbose_name=_("Зураг"))

    class Meta:
        verbose_name = _("Пайз")
        verbose_name_plural = _("Пайз")

    def __str__(self):
        return self.paizName

class Product(models.Model):
    prodName = models.CharField(max_length=50, verbose_name=_("Барааны нэр"))
    zCode = models.IntegerField(null=True, blank=True, verbose_name=_("Зураасан код"))
    prodType = models.ForeignKey(ProdType, related_name='products',on_delete=models.CASCADE, verbose_name=_("Төрлийн нэр"))
    zzCode = models.IntegerField(null=True, blank=True, verbose_name=_("Нэмэлт зураасан код"))
    price = models.IntegerField(null=True, blank=True, verbose_name=_("Үнэ"))
    hemNegj = models.IntegerField(null=True, blank=True, verbose_name=_("Хэмжих нэгж"))
    hudNegj = models.IntegerField(null=True, blank=True, verbose_name=_("Худалдан авалтын нэгж"))
    company = models.ForeignKey(Company,related_name='products', on_delete=models.CASCADE, verbose_name=_("Компани"))
    erNershil = models.CharField(max_length=50, verbose_name=_("Ерөнхий нэршил"))
    emHelber = models.CharField(max_length=50, verbose_name=_("Эмийн хэлбэр"))
    paiz = models.ForeignKey(Paiz, on_delete=models.CASCADE,verbose_name=_("Пайз"))
    uildwerlegch = models.CharField(max_length=50, verbose_name=_("Үйлдвэрлэгч"))
    uNiiluulegch = models.CharField(max_length=50, verbose_name=_("Үндсэн нийлүүлэгч"))
    # category = models.CharField(max_length=50, verbose_name=_("Дотоод ангилал"))
    category = models.ForeignKey(Category,related_name='products', on_delete=models.CASCADE,verbose_name=_("Ангилал"))
    borBoloh = models.BooleanField(verbose_name=_("Борлуулж болох эсэх"),default=False)
    hudAwch = models.BooleanField(verbose_name=_("Худалдан авч болох эсэх"),default=False)
    state = models.ForeignKey(State,related_name='products', on_delete=models.CASCADE, verbose_name=_("Төлөв"))

    class Meta:
        verbose_name = _("Бараа")
        verbose_name_plural = _("Бараа")

    def __str__(self):
        # return self.prodName+" "+str(self.state.stateName)
        return '%s %s %s %s %s %s' % (self.prodName, self.prodType, self.price,self.category, self.state, self.company)



        