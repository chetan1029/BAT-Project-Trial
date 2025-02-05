# Generated by Django 2.1.4 on 2019-01-23 09:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0023_auto_20190123_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amazonmarket',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 23, 9, 53, 19, 171045, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='amazonmarket',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 23, 9, 53, 19, 171087, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='amazonmwsauth',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 23, 9, 53, 19, 171451, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='amazonmwsauth',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 23, 9, 53, 19, 171468, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='box',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 23, 9, 53, 19, 170680, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='box',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 23, 9, 53, 19, 170697, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='currency',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 23, 9, 53, 19, 170359, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='currency',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 23, 9, 53, 19, 170378, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='status',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 23, 9, 53, 19, 169905, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='status',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 23, 9, 53, 19, 170019, tzinfo=utc)),
        ),
    ]
