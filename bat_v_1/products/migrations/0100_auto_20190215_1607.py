# Generated by Django 2.1.4 on 2019-02-15 16:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0099_auto_20190215_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amazonproduct',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 16, 7, 47, 871806, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='amazonproduct',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 16, 7, 47, 871822, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='packagemeasurement',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 16, 7, 47, 870750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='packagemeasurement',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 16, 7, 47, 870769, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 16, 7, 47, 869913, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 16, 7, 47, 869938, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='productbundle',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 16, 7, 47, 871196, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='productbundle',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 16, 7, 47, 871213, tzinfo=utc)),
        ),
    ]
