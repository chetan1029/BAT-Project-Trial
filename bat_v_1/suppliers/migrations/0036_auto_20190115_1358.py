# Generated by Django 2.1.4 on 2019-01-15 13:58

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0035_auto_20190115_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aql',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 15, 13, 58, 19, 961027, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aql',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 15, 13, 58, 19, 961048, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aqlfile',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 15, 13, 58, 19, 961573, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aqlfile',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 15, 13, 58, 19, 961592, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aqlproduct',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 15, 13, 58, 19, 962028, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aqlproduct',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 15, 13, 58, 19, 962046, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bank',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 15, 13, 58, 19, 957320, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bank',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 15, 13, 58, 19, 957340, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='category',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 15, 13, 58, 19, 953831, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='category',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 15, 13, 58, 19, 953856, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 15, 13, 58, 19, 956609, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 15, 13, 58, 19, 956629, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contract',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 15, 13, 58, 19, 957950, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contract',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 15, 13, 58, 19, 957998, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='currency',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 15, 13, 58, 19, 956124, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='currency',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 15, 13, 58, 19, 956145, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='mold',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 15, 13, 58, 19, 959379, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='mold',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 15, 13, 58, 19, 959396, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='moldfile',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 15, 13, 58, 19, 960539, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='moldfile',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 15, 13, 58, 19, 960558, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='moldproduct',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 15, 13, 58, 19, 959998, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='moldproduct',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 15, 13, 58, 19, 960017, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 15, 13, 58, 19, 962657, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 15, 13, 58, 19, 962674, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderdelivery',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 15, 13, 58, 19, 964918, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderdelivery',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suppliers.Order', verbose_name='Select Order'),
        ),
        migrations.AlterField(
            model_name='orderdelivery',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 15, 13, 58, 19, 964933, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderfile',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 15, 13, 58, 19, 963838, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderfile',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suppliers.Order', verbose_name='Select Order'),
        ),
        migrations.AlterField(
            model_name='orderfile',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 15, 13, 58, 19, 963859, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderpayment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 15, 13, 58, 19, 964356, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderpayment',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suppliers.Order', verbose_name='Select Order'),
        ),
        migrations.AlterField(
            model_name='orderpayment',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 15, 13, 58, 19, 964372, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 15, 13, 58, 19, 963364, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suppliers.Order', verbose_name='Select Order'),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 15, 13, 58, 19, 963382, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='paymentterms',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 15, 13, 58, 19, 955182, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='paymentterms',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 15, 13, 58, 19, 955203, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='productprice',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 15, 13, 58, 19, 958502, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='productprice',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 15, 13, 58, 19, 958559, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='status',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 15, 13, 58, 19, 955661, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='status',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 15, 13, 58, 19, 955687, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 15, 13, 58, 19, 954499, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 15, 13, 58, 19, 954520, tzinfo=utc)),
        ),
    ]
