# Generated by Django 2.1.4 on 2019-02-15 07:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0087_auto_20190214_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 7, 47, 40, 350632, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 7, 47, 40, 350647, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shipmentfiles',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 7, 47, 40, 351848, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shipmentfiles',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 7, 47, 40, 351866, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shipmentfullfillment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 7, 47, 40, 349906, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shipmentfullfillment',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 7, 47, 40, 349924, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shipmentproduct',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 7, 47, 40, 351380, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shipmentproduct',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 7, 47, 40, 351400, tzinfo=utc)),
        ),
    ]
