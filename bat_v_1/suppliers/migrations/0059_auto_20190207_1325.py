# Generated by Django 2.1.4 on 2019-02-07 13:25

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0058_auto_20190207_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aql',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='settings.Category', verbose_name='Select Categories'),
        ),
        migrations.AlterField(
            model_name='aql',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 7, 13, 25, 22, 303921, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aql',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 7, 13, 25, 22, 303938, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aqlfile',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 7, 13, 25, 22, 304369, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aqlfile',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 7, 13, 25, 22, 304385, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bank',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 7, 13, 25, 22, 299998, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bank',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 7, 13, 25, 22, 300015, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 7, 13, 25, 22, 299437, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 7, 13, 25, 22, 299458, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contract',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 7, 13, 25, 22, 300974, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contract',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 7, 13, 25, 22, 300991, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='mold',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 7, 13, 25, 22, 302046, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='mold',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 7, 13, 25, 22, 302062, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='moldfile',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 7, 13, 25, 22, 302981, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='moldfile',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 7, 13, 25, 22, 302998, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='moldhost',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 7, 13, 25, 22, 303458, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='moldhost',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 7, 13, 25, 22, 303474, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 7, 13, 25, 22, 304835, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 7, 13, 25, 22, 304852, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderdelivery',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 7, 13, 25, 22, 306923, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderdelivery',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 7, 13, 25, 22, 306939, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderfile',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 7, 13, 25, 22, 305884, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderfile',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 7, 13, 25, 22, 305900, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderpayment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 7, 13, 25, 22, 306340, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderpayment',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 7, 13, 25, 22, 306356, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 7, 13, 25, 22, 305432, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 7, 13, 25, 22, 305449, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='paymentterms',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 7, 13, 25, 22, 297995, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='paymentterms',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 7, 13, 25, 22, 298014, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='productprice',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 7, 13, 25, 22, 301498, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='productprice',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 7, 13, 25, 22, 301515, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 7, 13, 25, 22, 298691, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 7, 13, 25, 22, 298709, tzinfo=utc)),
        ),
    ]
