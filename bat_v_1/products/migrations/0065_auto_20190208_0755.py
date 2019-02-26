# Generated by Django 2.1.4 on 2019-02-08 07:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0064_auto_20190208_0741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amazonproduct',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 8, 7, 55, 40, 232792, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='amazonproduct',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 8, 7, 55, 40, 232812, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='packagemeasurement',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 8, 7, 55, 40, 231798, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='packagemeasurement',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 8, 7, 55, 40, 231821, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 8, 7, 55, 40, 230938, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 8, 7, 55, 40, 230956, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='productbundle',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 8, 7, 55, 40, 232246, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='productbundle',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 8, 7, 55, 40, 232262, tzinfo=utc)),
        ),
    ]
