# Generated by Django 3.1.7 on 2021-06-14 05:56

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catName', models.CharField(max_length=50, verbose_name='Ангилалын нэр')),
            ],
            options={
                'verbose_name': 'Ангилал',
                'verbose_name_plural': 'Ангилал',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comName', models.CharField(max_length=50, verbose_name='Компаний нэр')),
                ('hayag', models.CharField(max_length=150, verbose_name='Компаний хаяг')),
                ('phone', models.CharField(max_length=30, verbose_name='Компаний утас')),
            ],
            options={
                'verbose_name': 'Компани',
                'verbose_name_plural': 'Компани',
            },
        ),
        migrations.CreateModel(
            name='HereglegchRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('levelName', models.CharField(max_length=300, verbose_name='Эрхийн түвшин')),
            ],
            options={
                'verbose_name': 'Эрхийн түвшин',
                'verbose_name_plural': 'Эрхийн түвшин',
            },
        ),
        migrations.CreateModel(
            name='HereglegchState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stateName', models.CharField(max_length=300, verbose_name='Хэрэглэгч төлөв')),
            ],
            options={
                'verbose_name': 'Хэрэглэгч төлөв',
                'verbose_name_plural': 'Хэрэглэгч төлөв',
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manName', models.CharField(max_length=50, verbose_name='Үйлдвэрлэгчийн нэр')),
                ('manPic', models.ImageField(upload_to='media/manufacturer/', verbose_name='Зураг')),
            ],
            options={
                'verbose_name': 'Үйлдвэрлэгч',
                'verbose_name_plural': 'Үйлдвэрлэгч',
            },
        ),
        migrations.CreateModel(
            name='Paiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paizName', models.CharField(max_length=50, verbose_name='Пайзын нэр')),
                ('paizKey', models.CharField(max_length=50, verbose_name='Пайзын түлхүүр')),
                ('description', models.TextField(verbose_name='Тайлбар')),
                ('ontslohEseh', models.BooleanField(verbose_name='Онцлох эсэх')),
                ('picPaiz', models.ImageField(upload_to='media/paiz/', verbose_name='Зураг')),
            ],
            options={
                'verbose_name': 'Пайз',
                'verbose_name_plural': 'Пайз',
            },
        ),
        migrations.CreateModel(
            name='ProdType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeName', models.CharField(max_length=50, verbose_name='Төрлийн нэр')),
            ],
            options={
                'verbose_name': 'Барааны төрөл',
                'verbose_name_plural': 'Барааны төрөл',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stateName', models.CharField(max_length=50, verbose_name='Төлөвийн нэр')),
            ],
            options={
                'verbose_name': 'Барааны төлөв',
                'verbose_name_plural': 'Барааны төлөв',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prodName', models.CharField(max_length=50, verbose_name='Барааны нэр')),
                ('zCode', models.IntegerField(blank=True, null=True, verbose_name='Зураасан код')),
                ('zzCode', models.IntegerField(blank=True, null=True, verbose_name='Нэмэлт зураасан код')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='Үнэ')),
                ('hemNegj', models.IntegerField(blank=True, null=True, verbose_name='Хэмжих нэгж')),
                ('hudNegj', models.IntegerField(blank=True, null=True, verbose_name='Худалдан авалтын нэгж')),
                ('erNershil', models.CharField(max_length=50, verbose_name='Ерөнхий нэршил')),
                ('emHelber', models.CharField(max_length=50, verbose_name='Эмийн хэлбэр')),
                ('uildwerlegch', models.CharField(max_length=50, verbose_name='Үйлдвэрлэгч')),
                ('uNiiluulegch', models.CharField(max_length=50, verbose_name='Үндсэн нийлүүлэгч')),
                ('borBoloh', models.BooleanField(verbose_name='Борлуулж болох эсэх')),
                ('hudAwch', models.BooleanField(verbose_name='Худалдан авч болох эсэх')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='BMweb.category', verbose_name='Ангилал')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='BMweb.company', verbose_name='Компани')),
                ('paiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BMweb.paiz', verbose_name='Пайз')),
                ('prodType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='BMweb.prodtype', verbose_name='Төрлийн нэр')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='BMweb.state', verbose_name='Төлөв')),
            ],
            options={
                'verbose_name': 'Бараа',
                'verbose_name_plural': 'Бараа',
            },
        ),
        migrations.CreateModel(
            name='ProdBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brandName', models.CharField(max_length=50, verbose_name='Бренд нэр')),
                ('brandCode', models.CharField(max_length=50, verbose_name='Бренд код')),
                ('slug', models.SlugField()),
                ('description', models.TextField(verbose_name='Тайлбар')),
                ('ontslohEseh', models.BooleanField(verbose_name='Онцлох эсэх')),
                ('idewhiteiEseh', models.BooleanField(verbose_name='Идэвхитэй эсэх')),
                ('pic', models.ImageField(upload_to='media/brand/', verbose_name='Зураг')),
                ('picBig', models.ImageField(upload_to='media/brand/', verbose_name='Том зураг')),
                ('thumbimage', models.ImageField(upload_to='media/brandthumb/', verbose_name='Зураг')),
                ('erembe', models.IntegerField(blank=True, null=True, verbose_name='Эрэмбэ')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BMweb.category', verbose_name='Ангилал')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BMweb.manufacturer', verbose_name='Үйлдвэрлэгч')),
            ],
            options={
                'verbose_name': 'Бүтээгдэхүүний бренд',
                'verbose_name_plural': 'Бүтээгдэхүүний бренд',
            },
        ),
        migrations.CreateModel(
            name='Hereglegch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ovog', models.CharField(max_length=30, verbose_name='Хэрэглэгчийн  овог')),
                ('ner', models.CharField(max_length=30, verbose_name='Хэрэглэгчийн нэр')),
                ('mail', models.CharField(max_length=30, verbose_name='мейл хаяг')),
                ('password', models.CharField(max_length=30, verbose_name='Хэрэглэгчийн  нууц үг')),
                ('reg_date', models.DateTimeField(default=datetime.datetime.now)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BMweb.company')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BMweb.hereglegchrole')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BMweb.hereglegchstate')),
            ],
            options={
                'verbose_name': 'Хэрэглэгч',
                'verbose_name_plural': 'Хэрэглэгч',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Харилцагчийн нэр')),
                ('code', models.CharField(max_length=30, verbose_name='Харилцагчийн код')),
                ('mail', models.CharField(max_length=50, verbose_name='Компаний майл')),
                ('password', models.CharField(max_length=50, verbose_name='Майлын нууц үг')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BMweb.company')),
            ],
            options={
                'verbose_name': 'Харилцагч',
                'verbose_name_plural': 'Харилцагч',
            },
        ),
    ]
