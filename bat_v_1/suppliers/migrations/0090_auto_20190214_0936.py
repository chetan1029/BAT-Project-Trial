# Generated by Django 2.1.4 on 2019-02-14 09:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import suppliers.models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0089_auto_20190214_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aql',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 14, 9, 36, 2, 21842, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aql',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 14, 9, 36, 2, 21859, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bank',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 14, 9, 36, 2, 17863, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bank',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 14, 9, 36, 2, 17880, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='certification',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 14, 9, 36, 2, 25683, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='certification',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 14, 9, 36, 2, 25700, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 14, 9, 36, 2, 17316, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 14, 9, 36, 2, 17334, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contract',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 14, 9, 36, 2, 18873, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contract',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 14, 9, 36, 2, 18889, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='mold',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 14, 9, 36, 2, 19907, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='mold',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 14, 9, 36, 2, 19923, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='moldfile',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 14, 9, 36, 2, 20913, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='moldfile',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 14, 9, 36, 2, 20930, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='moldhost',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 14, 9, 36, 2, 21335, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='moldhost',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 14, 9, 36, 2, 21351, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 14, 9, 36, 2, 22462, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 14, 9, 36, 2, 22494, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderdelivery',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 14, 9, 36, 2, 24784, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderdelivery',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 14, 9, 36, 2, 24751, tzinfo=utc), verbose_name='Select Delivery date'),
        ),
        migrations.AlterField(
            model_name='orderdelivery',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 14, 9, 36, 2, 24798, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderdeliveryproduct',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 14, 9, 36, 2, 25266, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderdeliveryproduct',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 14, 9, 36, 2, 25282, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderfile',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 14, 9, 36, 2, 23648, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderfile',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 14, 9, 36, 2, 23664, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderpayment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 14, 9, 36, 2, 24116, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderpayment',
            name='file_url',
            field=models.FileField(blank=True, upload_to=suppliers.models.generate_orderpaymentfilename),
        ),
        migrations.AlterField(
            model_name='orderpayment',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 14, 9, 36, 2, 24132, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 14, 9, 36, 2, 23153, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 14, 9, 36, 2, 23170, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='paymentterms',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 14, 9, 36, 2, 16057, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='paymentterms',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 14, 9, 36, 2, 16077, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='productprice',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 14, 9, 36, 2, 19362, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='productprice',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 14, 9, 36, 2, 19378, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 14, 9, 36, 2, 16669, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 14, 9, 36, 2, 16686, tzinfo=utc)),
        ),
    ]
