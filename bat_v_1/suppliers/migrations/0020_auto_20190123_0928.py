# Generated by Django 2.1.4 on 2019-01-23 09:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0019_auto_20190123_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aql',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 23, 9, 28, 6, 789594, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aql',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 23, 9, 28, 6, 789610, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aqlfile',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 23, 9, 28, 6, 789959, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aqlfile',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 23, 9, 28, 6, 789976, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aqlproduct',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 23, 9, 28, 6, 790340, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aqlproduct',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 23, 9, 28, 6, 790357, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bank',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 23, 9, 28, 6, 786685, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bank',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 23, 9, 28, 6, 786703, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 23, 9, 28, 6, 786030, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 23, 9, 28, 6, 786047, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contract',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 23, 9, 28, 6, 787191, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contract',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 23, 9, 28, 6, 787207, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='mold',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 23, 9, 28, 6, 788242, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='mold',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 23, 9, 28, 6, 788257, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='moldfile',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 23, 9, 28, 6, 789144, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='moldfile',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 23, 9, 28, 6, 789164, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='moldproduct',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 23, 9, 28, 6, 788735, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='moldproduct',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 23, 9, 28, 6, 788752, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 23, 9, 28, 6, 790811, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 23, 9, 28, 6, 790832, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderdelivery',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 23, 9, 28, 6, 792900, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderdelivery',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 23, 9, 28, 6, 792916, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderfile',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 23, 9, 28, 6, 791866, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderfile',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 23, 9, 28, 6, 791883, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderpayment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 23, 9, 28, 6, 792322, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderpayment',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 23, 9, 28, 6, 792340, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 23, 9, 28, 6, 791336, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 23, 9, 28, 6, 791367, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='paymentterms',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 23, 9, 28, 6, 784663, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='paymentterms',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 23, 9, 28, 6, 784687, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='productprice',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 23, 9, 28, 6, 787680, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='productprice',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 23, 9, 28, 6, 787697, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 23, 9, 28, 6, 785341, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 23, 9, 28, 6, 785375, tzinfo=utc)),
        ),
    ]
