# Generated by Django 2.1.4 on 2019-02-16 13:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0100_auto_20190215_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amazonproduct',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 16, 13, 49, 41, 647952, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='amazonproduct',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 16, 13, 49, 41, 647970, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='packagemeasurement',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 16, 13, 49, 41, 646923, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='packagemeasurement',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 16, 13, 49, 41, 646940, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 16, 13, 49, 41, 646317, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 16, 13, 49, 41, 646339, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='productbundle',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 16, 13, 49, 41, 647356, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='productbundle',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 16, 13, 49, 41, 647372, tzinfo=utc)),
        ),
    ]
