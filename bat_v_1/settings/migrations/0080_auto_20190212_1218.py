# Generated by Django 2.1.4 on 2019-02-12 12:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0079_auto_20190212_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amazonmarket',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 12, 18, 54, 163676, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='amazonmarket',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 12, 18, 54, 163693, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='amazonmwsauth',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 12, 18, 54, 164066, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='amazonmwsauth',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 12, 18, 54, 164083, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='box',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 12, 18, 54, 163274, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='box',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 12, 18, 54, 163292, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='currency',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 12, 18, 54, 162803, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='currency',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 12, 18, 54, 162822, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='status',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 12, 18, 54, 162379, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='status',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 12, 18, 54, 162408, tzinfo=utc)),
        ),
    ]
