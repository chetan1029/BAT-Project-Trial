# Generated by Django 2.1.4 on 2019-01-21 09:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20190121_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amazonproduct',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 21, 9, 48, 0, 719090, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='amazonproduct',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 21, 9, 48, 0, 719106, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='packagemeasurement',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 21, 9, 48, 0, 718077, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='packagemeasurement',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 21, 9, 48, 0, 718095, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 21, 9, 48, 0, 717313, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 21, 9, 48, 0, 717331, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='productbundle',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 21, 9, 48, 0, 718548, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='productbundle',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 21, 9, 48, 0, 718565, tzinfo=utc)),
        ),
    ]
