# Generated by Django 2.1.4 on 2019-01-16 10:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20190116_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 16, 10, 14, 4, 219196, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='currency',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 16, 10, 14, 4, 219214, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='packagemeasurement',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 16, 10, 14, 4, 220276, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='packagemeasurement',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 16, 10, 14, 4, 220292, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 16, 10, 14, 4, 219627, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 16, 10, 14, 4, 219643, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='productbundle',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 16, 10, 14, 4, 220762, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='productbundle',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 16, 10, 14, 4, 220778, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='status',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 16, 10, 14, 4, 218846, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='status',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 16, 10, 14, 4, 218877, tzinfo=utc)),
        ),
    ]
