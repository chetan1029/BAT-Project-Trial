# Generated by Django 2.1.4 on 2019-02-19 13:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0100_auto_20190219_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 19, 13, 12, 0, 885938, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 19, 13, 12, 0, 885953, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shipmentfiles',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 19, 13, 12, 0, 887219, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shipmentfiles',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 19, 13, 12, 0, 887237, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shipmentfullfillment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 19, 13, 12, 0, 885267, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shipmentfullfillment',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 19, 13, 12, 0, 885286, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shipmentproduct',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 19, 13, 12, 0, 886762, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shipmentproduct',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 19, 13, 12, 0, 886779, tzinfo=utc)),
        ),
    ]
