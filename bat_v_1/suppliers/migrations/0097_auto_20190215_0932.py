# Generated by Django 2.1.4 on 2019-02-15 09:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0096_auto_20190215_0911'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproduct',
            name='remaining_quantity',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='aql',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 32, 28, 452686, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aql',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 32, 28, 452707, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bank',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 32, 28, 448762, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bank',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 32, 28, 448784, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='certification',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 32, 28, 456485, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='certification',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 32, 28, 456501, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 32, 28, 448146, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 32, 28, 448166, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contract',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 32, 28, 449792, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contract',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 32, 28, 449813, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='mold',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 32, 28, 450793, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='mold',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 32, 28, 450809, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='moldfile',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 32, 28, 451780, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='moldfile',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 32, 28, 451797, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='moldhost',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 32, 28, 452204, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='moldhost',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 32, 28, 452225, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 32, 28, 453234, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 32, 28, 453309, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderdelivery',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 32, 28, 454805, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderdelivery',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 32, 28, 454740, tzinfo=utc), verbose_name='Select Delivery date'),
        ),
        migrations.AlterField(
            model_name='orderdelivery',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 32, 28, 454819, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderdeliveryproduct',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 32, 28, 456050, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderdeliveryproduct',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 32, 28, 456067, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderfile',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 32, 28, 454360, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderfile',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 32, 28, 454377, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderpayment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 32, 28, 455444, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderpayment',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 32, 28, 455460, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 32, 28, 453861, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 32, 28, 453881, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='paymentterms',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 32, 28, 446655, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='paymentterms',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 32, 28, 446679, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='productprice',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 32, 28, 450239, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='productprice',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 32, 28, 450260, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 32, 28, 447380, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 32, 28, 447398, tzinfo=utc)),
        ),
    ]
