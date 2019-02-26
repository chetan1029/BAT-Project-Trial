# Generated by Django 2.1.4 on 2019-01-21 10:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0013_auto_20190121_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aql',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 21, 10, 13, 39, 87121, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aql',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 21, 10, 13, 39, 87150, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aqlfile',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 21, 10, 13, 39, 87583, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aqlfile',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 21, 10, 13, 39, 87600, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aqlproduct',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 21, 10, 13, 39, 87976, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aqlproduct',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 21, 10, 13, 39, 87997, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bank',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 21, 10, 13, 39, 83692, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bank',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 21, 10, 13, 39, 83728, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 21, 10, 13, 39, 82958, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 21, 10, 13, 39, 82978, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contract',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 21, 10, 13, 39, 84279, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contract',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 21, 10, 13, 39, 84295, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='mold',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 21, 10, 13, 39, 85342, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='mold',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 21, 10, 13, 39, 85358, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='moldfile',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 21, 10, 13, 39, 86610, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='moldfile',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 21, 10, 13, 39, 86629, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='moldproduct',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 21, 10, 13, 39, 85971, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='moldproduct',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 21, 10, 13, 39, 85989, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 21, 10, 13, 39, 88619, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 21, 10, 13, 39, 88638, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderdelivery',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 21, 10, 13, 39, 91284, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderdelivery',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 21, 10, 13, 39, 91304, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderfile',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 21, 10, 13, 39, 89861, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderfile',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 21, 10, 13, 39, 89879, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderpayment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 21, 10, 13, 39, 90685, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderpayment',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 21, 10, 13, 39, 90700, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 21, 10, 13, 39, 89332, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 21, 10, 13, 39, 89352, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='paymentterms',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 21, 10, 13, 39, 81798, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='paymentterms',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 21, 10, 13, 39, 81820, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='productprice',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 21, 10, 13, 39, 84715, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='productprice',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 21, 10, 13, 39, 84731, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 21, 10, 13, 39, 82353, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 21, 10, 13, 39, 82374, tzinfo=utc)),
        ),
    ]
