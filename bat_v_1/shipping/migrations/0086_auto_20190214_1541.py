# Generated by Django 2.1.4 on 2019-02-14 15:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0085_auto_20190214_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 14, 15, 41, 48, 227959, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 14, 15, 41, 48, 227979, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shipmentfiles',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 14, 15, 41, 48, 229241, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shipmentfiles',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 14, 15, 41, 48, 229258, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shipmentfullfillment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 14, 15, 41, 48, 226143, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shipmentfullfillment',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 14, 15, 41, 48, 226160, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shipmentproduct',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 14, 15, 41, 48, 228771, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shipmentproduct',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 14, 15, 41, 48, 228788, tzinfo=utc)),
        ),
    ]
