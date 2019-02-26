# Generated by Django 2.1.4 on 2019-02-25 07:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0114_auto_20190222_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amazonproduct',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 25, 7, 11, 9, 860835, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='amazonproduct',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 25, 7, 11, 9, 860852, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='box',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 25, 7, 11, 9, 860237, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='box',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 25, 7, 11, 9, 860253, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='packagemeasurement',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 25, 7, 11, 9, 859353, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='packagemeasurement',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 25, 7, 11, 9, 859369, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 25, 7, 11, 9, 858745, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 25, 7, 11, 9, 858763, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='productbundle',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 25, 7, 11, 9, 859786, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='productbundle',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 25, 7, 11, 9, 859803, tzinfo=utc)),
        ),
    ]
