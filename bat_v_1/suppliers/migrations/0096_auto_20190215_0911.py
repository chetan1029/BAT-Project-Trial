# Generated by Django 2.1.4 on 2019-02-15 09:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0095_auto_20190215_0749'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdelivery',
            name='share_percentage',
            field=models.FloatField(default='0'),
        ),
        migrations.AddField(
            model_name='orderdeliveryproduct',
            name='share_percentage',
            field=models.FloatField(default='0'),
        ),
        migrations.AddField(
            model_name='orderpayment',
            name='share_percentage',
            field=models.FloatField(default='0'),
        ),
        migrations.AlterField(
            model_name='aql',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 11, 17, 617456, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aql',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 11, 17, 617475, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bank',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 11, 17, 613676, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bank',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 11, 17, 613696, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='certification',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 11, 17, 621232, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='certification',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 11, 17, 621253, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 11, 17, 613146, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 11, 17, 613163, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contract',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 11, 17, 614650, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contract',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 11, 17, 614671, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='mold',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 11, 17, 615627, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='mold',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 11, 17, 615643, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='moldfile',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 11, 17, 616569, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='moldfile',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 11, 17, 616585, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='moldhost',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 11, 17, 616976, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='moldhost',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 11, 17, 616996, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 11, 17, 617972, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 11, 17, 618048, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderdelivery',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 11, 17, 619461, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderdelivery',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 11, 17, 619398, tzinfo=utc), verbose_name='Select Delivery date'),
        ),
        migrations.AlterField(
            model_name='orderdelivery',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 11, 17, 619475, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderdeliveryproduct',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 11, 17, 620664, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderdeliveryproduct',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 11, 17, 620680, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderfile',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 11, 17, 619035, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderfile',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 11, 17, 619051, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderpayment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 11, 17, 620084, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderpayment',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 11, 17, 620099, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 11, 17, 618565, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 11, 17, 618581, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='paymentterms',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 11, 17, 612000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='paymentterms',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 11, 17, 612021, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='productprice',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 11, 17, 615087, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='productprice',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 11, 17, 615107, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 11, 17, 612543, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 15, 9, 11, 17, 612559, tzinfo=utc)),
        ),
    ]
