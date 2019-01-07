# Generated by Django 2.1.4 on 2019-01-07 12:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20190104_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='users/profile/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 7, 12, 26, 17, 650841, tzinfo=utc)),
        ),
    ]
