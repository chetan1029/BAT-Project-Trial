# Generated by Django 2.1.4 on 2019-01-10 14:48

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20190110_1448'),
        ('suppliers', '0015_auto_20190110_1415'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mold',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('x_units', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=3, max_digits=7)),
                ('no_of_layers', models.IntegerField()),
                ('production_date', models.DateTimeField()),
                ('create_date', models.DateTimeField(default=datetime.datetime(2019, 1, 10, 14, 48, 16, 108371, tzinfo=utc))),
                ('update_date', models.DateTimeField(default=datetime.datetime(2019, 1, 10, 14, 48, 16, 108386, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='MoldProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(default=datetime.datetime(2019, 1, 10, 14, 48, 16, 108868, tzinfo=utc))),
                ('update_date', models.DateTimeField(default=datetime.datetime(2019, 1, 10, 14, 48, 16, 108885, tzinfo=utc))),
                ('mold', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='suppliers.Mold', verbose_name='Select Mold')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.Product', verbose_name='Select Product')),
            ],
        ),
        migrations.AlterField(
            model_name='bank',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 10, 14, 48, 16, 106988, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bank',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 10, 14, 48, 16, 107005, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='category',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 10, 14, 48, 16, 103987, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='category',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 10, 14, 48, 16, 104010, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 10, 14, 48, 16, 106423, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 10, 14, 48, 16, 106439, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contract',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 10, 14, 48, 16, 107443, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contract',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 10, 14, 48, 16, 107460, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='currency',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 10, 14, 48, 16, 106067, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='currency',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 10, 14, 48, 16, 106084, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='paymentterms',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 10, 14, 48, 16, 105408, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='paymentterms',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 10, 14, 48, 16, 105427, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='productprice',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 10, 14, 48, 16, 107861, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='productprice',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 10, 14, 48, 16, 107878, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='status',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 10, 14, 48, 16, 105770, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='status',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 10, 14, 48, 16, 105802, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 10, 14, 48, 16, 104657, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 10, 14, 48, 16, 104675, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='mold',
            name='currency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='suppliers.Currency', verbose_name='Select Currency'),
        ),
        migrations.AddField(
            model_name='mold',
            name='mold_supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='mold_supplier', to='suppliers.Supplier', verbose_name='Select Mold Supplier'),
        ),
        migrations.AddField(
            model_name='mold',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='suppliers.Supplier', verbose_name='Select Supplier'),
        ),
    ]
