# Generated by Django 2.1.4 on 2019-02-06 07:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0040_auto_20190206_0740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 6, 7, 41, 28, 677278, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 6, 7, 41, 28, 677294, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shipmentfiles',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 6, 7, 41, 28, 678536, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shipmentfiles',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 6, 7, 41, 28, 678552, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shipmentfullfillment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 6, 7, 41, 28, 676647, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shipmentfullfillment',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 6, 7, 41, 28, 676665, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shipmentproduct',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 6, 7, 41, 28, 678028, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shipmentproduct',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 6, 7, 41, 28, 678048, tzinfo=utc)),
        ),
    ]
