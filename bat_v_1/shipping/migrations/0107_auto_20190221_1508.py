# Generated by Django 2.1.4 on 2019-02-21 15:08

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0113_auto_20190221_1508'),
        ('shipping', '0106_auto_20190221_1313'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShipmentProductOrderDelivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('create_date', models.DateTimeField(default=datetime.datetime(2019, 2, 21, 15, 8, 9, 110315, tzinfo=utc))),
                ('update_date', models.DateTimeField(default=datetime.datetime(2019, 2, 21, 15, 8, 9, 110332, tzinfo=utc))),
                ('orderdelivery', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='suppliers.OrderDelivery', verbose_name='Select Order Delivery')),
            ],
        ),
        migrations.RemoveField(
            model_name='shipment',
            name='order',
        ),
        migrations.AlterField(
            model_name='shipment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 21, 15, 8, 9, 108515, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='currency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='settings.Currency', verbose_name='Select Currency'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='invoice_agent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='invoice_agent', to='suppliers.Supplier', verbose_name='Select Invoice Agent'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='invoice_currency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='currency_invoice', to='settings.Currency', verbose_name='Select Invoice Currency'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='invoice_value',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='kg_cbm_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Kg/CBM Price'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='prepaid_vat',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Prepaid VAT'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 21, 15, 8, 9, 108534, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='vat_currency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='currency_vat', to='settings.Currency', verbose_name='Select VAT Currency'),
        ),
        migrations.AlterField(
            model_name='shipmentfiles',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 21, 15, 8, 9, 110885, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shipmentfiles',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 21, 15, 8, 9, 110904, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shipmentfullfillment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 21, 15, 8, 9, 107880, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shipmentfullfillment',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 21, 15, 8, 9, 107897, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shipmentproduct',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 21, 15, 8, 9, 109859, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shipmentproduct',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 21, 15, 8, 9, 109875, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='shipmentproductorderdelivery',
            name='shipmentproduct',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shipping.ShipmentProduct', verbose_name='Select Shipment Product'),
        ),
    ]
