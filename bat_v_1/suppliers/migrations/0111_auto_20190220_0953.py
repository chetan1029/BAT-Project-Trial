# Generated by Django 2.1.4 on 2019-02-20 09:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0110_auto_20190219_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aql',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 20, 9, 53, 41, 235935, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aql',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 20, 9, 53, 41, 235952, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bank',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 20, 9, 53, 41, 231749, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bank',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 20, 9, 53, 41, 231771, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='certification',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 20, 9, 53, 41, 242474, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='certification',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 20, 9, 53, 41, 242500, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 20, 9, 53, 41, 231160, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 20, 9, 53, 41, 231179, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contract',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 20, 9, 53, 41, 232755, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contract',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 20, 9, 53, 41, 232772, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='mold',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 20, 9, 53, 41, 233865, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='mold',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 20, 9, 53, 41, 233882, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='moldfile',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 20, 9, 53, 41, 234880, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='moldfile',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 20, 9, 53, 41, 234901, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='moldhost',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 20, 9, 53, 41, 235368, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='moldhost',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 20, 9, 53, 41, 235386, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 20, 9, 53, 41, 236620, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 20, 9, 53, 41, 236651, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderdelivery',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 20, 9, 53, 41, 238653, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderdelivery',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 20, 9, 53, 41, 238551, tzinfo=utc), verbose_name='Select Delivery date'),
        ),
        migrations.AlterField(
            model_name='orderdelivery',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 20, 9, 53, 41, 238681, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderdeliveryproduct',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 20, 9, 53, 41, 240269, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderdeliveryproduct',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 20, 9, 53, 41, 240287, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderdeliverytestreport',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 20, 9, 53, 41, 240822, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderdeliverytestreport',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 20, 9, 53, 41, 240840, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderfile',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 20, 9, 53, 41, 237976, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderfile',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 20, 9, 53, 41, 237994, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderpayment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 20, 9, 53, 41, 239313, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderpayment',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 20, 9, 53, 41, 239344, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 20, 9, 53, 41, 237258, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 20, 9, 53, 41, 237276, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='paymentterms',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 20, 9, 53, 41, 229733, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='paymentterms',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 20, 9, 53, 41, 229789, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='productprice',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 20, 9, 53, 41, 233204, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='productprice',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 20, 9, 53, 41, 233221, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 20, 9, 53, 41, 230430, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 20, 9, 53, 41, 230447, tzinfo=utc)),
        ),
    ]
