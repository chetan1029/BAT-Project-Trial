# Generated by Django 2.1.4 on 2019-01-17 10:04

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import suppliers.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0002_auto_20190117_1004'),
        ('settings', '0003_auto_20190117_1004'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aql',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=50)),
                ('detail', models.TextField(blank=True)),
                ('create_date', models.DateTimeField(default=datetime.datetime(2019, 1, 17, 10, 4, 21, 965358, tzinfo=utc))),
                ('update_date', models.DateTimeField(default=datetime.datetime(2019, 1, 17, 10, 4, 21, 965374, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='AqlFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('file_url', models.FileField(upload_to=suppliers.models.generate_aqlfilename)),
                ('create_date', models.DateTimeField(default=datetime.datetime(2019, 1, 17, 10, 4, 21, 965789, tzinfo=utc))),
                ('update_date', models.DateTimeField(default=datetime.datetime(2019, 1, 17, 10, 4, 21, 965808, tzinfo=utc))),
                ('aql', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='suppliers.Aql', verbose_name='Select AQL')),
            ],
        ),
        migrations.CreateModel(
            name='AqlProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(default=datetime.datetime(2019, 1, 17, 10, 4, 21, 966174, tzinfo=utc))),
                ('update_date', models.DateTimeField(default=datetime.datetime(2019, 1, 17, 10, 4, 21, 966190, tzinfo=utc))),
                ('aql', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='suppliers.Aql', verbose_name='Select AQL')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.Product', verbose_name='Select Product')),
            ],
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address1', models.CharField(max_length=200)),
                ('address2', models.CharField(blank=True, max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('zip', models.CharField(max_length=200, verbose_name='Zip/Pin Code')),
                ('region', models.CharField(blank=True, max_length=200, verbose_name='Region/State')),
                ('country', models.CharField(max_length=200)),
                ('benificary', models.CharField(max_length=100)),
                ('account_number', models.CharField(max_length=50)),
                ('swift_number', models.CharField(max_length=50)),
                ('swift_code', models.CharField(max_length=50)),
                ('create_date', models.DateTimeField(default=datetime.datetime(2019, 1, 17, 10, 4, 21, 962458, tzinfo=utc))),
                ('update_date', models.DateTimeField(default=datetime.datetime(2019, 1, 17, 10, 4, 21, 962474, tzinfo=utc))),
                ('currency', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='settings.Currency', verbose_name='Select Currency')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100)),
                ('skype', models.CharField(blank=True, max_length=50)),
                ('wechat', models.CharField(blank=True, max_length=50)),
                ('create_date', models.DateTimeField(default=datetime.datetime(2019, 1, 17, 10, 4, 21, 961928, tzinfo=utc))),
                ('update_date', models.DateTimeField(default=datetime.datetime(2019, 1, 17, 10, 4, 21, 961944, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('file_url', models.FileField(upload_to=suppliers.models.generate_filename)),
                ('create_date', models.DateTimeField(default=datetime.datetime(2019, 1, 17, 10, 4, 21, 962947, tzinfo=utc))),
                ('update_date', models.DateTimeField(default=datetime.datetime(2019, 1, 17, 10, 4, 21, 962963, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='Mold',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('x_units', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=3, max_digits=7)),
                ('no_of_layers', models.IntegerField()),
                ('paid_by', models.CharField(choices=[('Supplier', 'Supplier'), ('Us', 'Us')], default='', max_length=20)),
                ('production_date', models.DateField()),
                ('create_date', models.DateTimeField(default=datetime.datetime(2019, 1, 17, 10, 4, 21, 964039, tzinfo=utc))),
                ('update_date', models.DateTimeField(default=datetime.datetime(2019, 1, 17, 10, 4, 21, 964067, tzinfo=utc))),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='settings.Currency', verbose_name='Select Currency')),
            ],
        ),
        migrations.CreateModel(
            name='MoldFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('note', models.TextField(blank=True)),
                ('file_url', models.FileField(upload_to=suppliers.models.generate_moldfilename)),
                ('create_date', models.DateTimeField(default=datetime.datetime(2019, 1, 17, 10, 4, 21, 964963, tzinfo=utc))),
                ('update_date', models.DateTimeField(default=datetime.datetime(2019, 1, 17, 10, 4, 21, 964979, tzinfo=utc))),
                ('mold', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='suppliers.Mold', verbose_name='Select Mold')),
            ],
        ),
        migrations.CreateModel(
            name='MoldProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(default=datetime.datetime(2019, 1, 17, 10, 4, 21, 964550, tzinfo=utc))),
                ('update_date', models.DateTimeField(default=datetime.datetime(2019, 1, 17, 10, 4, 21, 964570, tzinfo=utc))),
                ('mold', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='suppliers.Mold', verbose_name='Select Mold')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.Product', verbose_name='Select Product')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(blank=True)),
                ('create_date', models.DateTimeField(default=datetime.datetime(2019, 1, 17, 10, 4, 21, 966649, tzinfo=utc))),
                ('update_date', models.DateTimeField(default=datetime.datetime(2019, 1, 17, 10, 4, 21, 966668, tzinfo=utc))),
                ('aql', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='suppliers.Aql', verbose_name='Select AQL')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='suppliers.Contact', verbose_name='Select Supplier Contact')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDelivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('file_url', models.FileField(blank=True, upload_to=suppliers.models.generate_orderdeliveryfilename)),
                ('create_date', models.DateTimeField(default=datetime.datetime(2019, 1, 17, 10, 4, 21, 968721, tzinfo=utc))),
                ('update_date', models.DateTimeField(default=datetime.datetime(2019, 1, 17, 10, 4, 21, 968737, tzinfo=utc))),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suppliers.Order', verbose_name='Select Order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('file_url', models.FileField(upload_to=suppliers.models.generate_orderfilename)),
                ('create_date', models.DateTimeField(default=datetime.datetime(2019, 1, 17, 10, 4, 21, 967703, tzinfo=utc))),
                ('update_date', models.DateTimeField(default=datetime.datetime(2019, 1, 17, 10, 4, 21, 967720, tzinfo=utc))),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suppliers.Order', verbose_name='Select Order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('invoice_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateTimeField(verbose_name='Select payment date')),
                ('note', models.TextField(blank=True)),
                ('file_url', models.FileField(upload_to=suppliers.models.generate_orderpaymentfilename)),
                ('create_date', models.DateTimeField(default=datetime.datetime(2019, 1, 17, 10, 4, 21, 968167, tzinfo=utc))),
                ('update_date', models.DateTimeField(default=datetime.datetime(2019, 1, 17, 10, 4, 21, 968182, tzinfo=utc))),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='suppliers.Bank', verbose_name='Select Bank')),
                ('invoice_currency', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='invoice_currency', to='settings.Currency', verbose_name='Select Invoice Currecy')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suppliers.Order', verbose_name='Select Order')),
                ('paid_currency', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='paid_currency', to='settings.Currency', verbose_name='Select Paid Currecy')),
            ],
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=3, max_digits=7)),
                ('quantity', models.IntegerField()),
                ('create_date', models.DateTimeField(default=datetime.datetime(2019, 1, 17, 10, 4, 21, 967191, tzinfo=utc))),
                ('update_date', models.DateTimeField(default=datetime.datetime(2019, 1, 17, 10, 4, 21, 967212, tzinfo=utc))),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='settings.Currency', verbose_name='Select Currency')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suppliers.Order', verbose_name='Select Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.Product', verbose_name='Select Product')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentTerms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('identifier', models.CharField(max_length=200)),
                ('prepay', models.DecimalField(decimal_places=2, max_digits=5)),
                ('days', models.IntegerField()),
                ('create_date', models.DateTimeField(default=datetime.datetime(2019, 1, 17, 10, 4, 21, 960776, tzinfo=utc))),
                ('update_date', models.DateTimeField(default=datetime.datetime(2019, 1, 17, 10, 4, 21, 960794, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='ProductPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=3, max_digits=7)),
                ('version', models.CharField(max_length=50)),
                ('create_date', models.DateTimeField(default=datetime.datetime(2019, 1, 17, 10, 4, 21, 963395, tzinfo=utc))),
                ('update_date', models.DateTimeField(default=datetime.datetime(2019, 1, 17, 10, 4, 21, 963411, tzinfo=utc))),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='settings.Currency', verbose_name='Select Currency')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.Product', verbose_name='Select Product')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='settings.Status', verbose_name='Select Status')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Supplier Name')),
                ('alternate_name', models.CharField(blank=True, max_length=200, verbose_name='Supplier Alternative Name')),
                ('logo', models.ImageField(blank=True, upload_to=suppliers.models.generate_logofilename)),
                ('address1', models.CharField(blank=True, max_length=200)),
                ('address2', models.CharField(blank=True, max_length=200)),
                ('city', models.CharField(blank=True, max_length=200)),
                ('zip', models.CharField(blank=True, max_length=200, verbose_name='Zip/Pin Code')),
                ('region', models.CharField(blank=True, max_length=200, verbose_name='Region/State')),
                ('country', models.CharField(blank=True, max_length=200)),
                ('detail', models.TextField(blank=True)),
                ('create_date', models.DateTimeField(default=datetime.datetime(2019, 1, 17, 10, 4, 21, 961281, tzinfo=utc))),
                ('update_date', models.DateTimeField(default=datetime.datetime(2019, 1, 17, 10, 4, 21, 961302, tzinfo=utc))),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.Category', verbose_name='Select Category')),
            ],
        ),
        migrations.AddField(
            model_name='productprice',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suppliers.Supplier', verbose_name='Select Supplier'),
        ),
        migrations.AddField(
            model_name='orderdelivery',
            name='orderpayment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suppliers.OrderPayment', verbose_name='Select Order Payment'),
        ),
        migrations.AddField(
            model_name='orderdelivery',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='settings.Status', verbose_name='Select Status'),
        ),
        migrations.AddField(
            model_name='order',
            name='paymentterms',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='suppliers.PaymentTerms', verbose_name='Select Payment Terms'),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='settings.Status', verbose_name='Select Status'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Select User'),
        ),
        migrations.AddField(
            model_name='mold',
            name='mold_supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='mold_supplier', to='suppliers.Supplier', verbose_name='Select Mold Supplier'),
        ),
        migrations.AddField(
            model_name='mold',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='suppliers.Supplier', verbose_name='Select Supplier'),
        ),
        migrations.AddField(
            model_name='contract',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suppliers.Supplier', verbose_name='Select Supplier'),
        ),
        migrations.AddField(
            model_name='contact',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suppliers.Supplier', verbose_name='Select Supplier'),
        ),
        migrations.AddField(
            model_name='bank',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suppliers.Supplier', verbose_name='Select Supplier'),
        ),
        migrations.AddField(
            model_name='aql',
            name='supplier',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='suppliers.Supplier', verbose_name='Select Supplier'),
        ),
        migrations.AlterUniqueTogether(
            name='aqlproduct',
            unique_together={('aql', 'product')},
        ),
    ]
