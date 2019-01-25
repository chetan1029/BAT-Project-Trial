# Generated by Django 2.1.4 on 2019-01-25 13:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0022_auto_20190125_0743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 25, 13, 32, 39, 67638, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 25, 13, 32, 39, 67656, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shipmentfiles',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 25, 13, 32, 39, 69320, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shipmentfiles',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 25, 13, 32, 39, 69339, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shipmentfullfillment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 25, 13, 32, 39, 66810, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shipmentfullfillment',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 25, 13, 32, 39, 66831, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shipmentproduct',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 25, 13, 32, 39, 68788, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shipmentproduct',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 25, 13, 32, 39, 68808, tzinfo=utc)),
        ),
    ]
