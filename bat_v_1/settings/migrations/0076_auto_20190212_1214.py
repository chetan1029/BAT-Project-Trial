# Generated by Django 2.1.4 on 2019-02-12 12:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0075_auto_20190212_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amazonmarket',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 12, 14, 45, 262905, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='amazonmarket',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 12, 14, 45, 262922, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='amazonmwsauth',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 12, 14, 45, 263343, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='amazonmwsauth',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 12, 14, 45, 263359, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='box',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 12, 14, 45, 262526, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='box',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 12, 14, 45, 262543, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='currency',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 12, 14, 45, 261898, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='currency',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 12, 14, 45, 262061, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='status',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 12, 14, 45, 261471, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='status',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 12, 14, 45, 261503, tzinfo=utc)),
        ),
    ]
