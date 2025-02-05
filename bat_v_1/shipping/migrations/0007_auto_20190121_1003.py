# Generated by Django 2.1.4 on 2019-01-21 10:03

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0006_auto_20190121_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='actual_vat',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, verbose_name='Actual VAT'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 21, 10, 3, 10, 240018, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='currency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='settings.Currency', verbose_name='Select Currency'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='invoice_agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='invoice_agent', to='suppliers.Supplier', verbose_name='Select Invoice Agent'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='invoice_currency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='currency_invoice', to='settings.Currency', verbose_name='Select Invoice Currency'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='suppliers.Order', verbose_name='Select Order'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 21, 10, 3, 10, 240034, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='vat_claimed',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, verbose_name='VAT Claimed'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='vat_currency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='currency_vat', to='settings.Currency', verbose_name='Select VAT Currency'),
        ),
    ]
