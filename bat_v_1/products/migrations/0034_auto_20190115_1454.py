# Generated by Django 2.1.4 on 2019-01-15 14:54

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0033_auto_20190115_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packagemeasurement',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 15, 14, 54, 14, 240850, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='packagemeasurement',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 15, 14, 54, 14, 240868, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.Category', verbose_name='Select Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='products.Color', verbose_name='Select Color'),
        ),
        migrations.AlterField(
            model_name='product',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 15, 14, 54, 14, 240185, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='products.Size', verbose_name='Select Size'),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='suppliers.Status', verbose_name='Select Status'),
        ),
        migrations.AlterField(
            model_name='product',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 15, 14, 54, 14, 240215, tzinfo=utc)),
        ),
    ]
