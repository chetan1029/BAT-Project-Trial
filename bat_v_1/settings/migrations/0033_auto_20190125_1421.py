# Generated by Django 2.1.4 on 2019-01-25 14:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0032_auto_20190125_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amazonmarket',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 25, 14, 21, 52, 370199, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='amazonmarket',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 25, 14, 21, 52, 370219, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='amazonmwsauth',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 25, 14, 21, 52, 370591, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='amazonmwsauth',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 25, 14, 21, 52, 370607, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='box',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 25, 14, 21, 52, 369834, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='box',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 25, 14, 21, 52, 369851, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='currency',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 25, 14, 21, 52, 369467, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='currency',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 25, 14, 21, 52, 369485, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='status',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 25, 14, 21, 52, 369008, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='status',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 25, 14, 21, 52, 369123, tzinfo=utc)),
        ),
    ]
