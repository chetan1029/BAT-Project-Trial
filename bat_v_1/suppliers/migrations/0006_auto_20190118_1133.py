# Generated by Django 2.1.4 on 2019-01-18 11:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0005_auto_20190117_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aql',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 18, 11, 33, 51, 624202, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aql',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 18, 11, 33, 51, 624218, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aqlfile',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 18, 11, 33, 51, 624580, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aqlfile',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 18, 11, 33, 51, 624596, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aqlproduct',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 18, 11, 33, 51, 625013, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aqlproduct',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 18, 11, 33, 51, 625030, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bank',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 18, 11, 33, 51, 621253, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bank',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 18, 11, 33, 51, 621271, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 18, 11, 33, 51, 620424, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 18, 11, 33, 51, 620451, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contract',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 18, 11, 33, 51, 621739, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contract',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 18, 11, 33, 51, 621756, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='mold',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 18, 11, 33, 51, 622811, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='mold',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 18, 11, 33, 51, 622827, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='moldfile',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 18, 11, 33, 51, 623797, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='moldfile',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 18, 11, 33, 51, 623817, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='moldproduct',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 18, 11, 33, 51, 623396, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='moldproduct',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 18, 11, 33, 51, 623417, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 18, 11, 33, 51, 625493, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 18, 11, 33, 51, 625509, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderdelivery',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 18, 11, 33, 51, 627742, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderdelivery',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 18, 11, 33, 51, 627759, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderfile',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 18, 11, 33, 51, 626492, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderfile',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 18, 11, 33, 51, 626509, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderpayment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 18, 11, 33, 51, 627044, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderpayment',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 18, 11, 33, 51, 627060, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 18, 11, 33, 51, 626009, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 18, 11, 33, 51, 626025, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='paymentterms',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 18, 11, 33, 51, 619371, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='paymentterms',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 18, 11, 33, 51, 619392, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='productprice',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 18, 11, 33, 51, 622185, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='productprice',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 18, 11, 33, 51, 622201, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 18, 11, 33, 51, 619821, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 18, 11, 33, 51, 619837, tzinfo=utc)),
        ),
    ]
