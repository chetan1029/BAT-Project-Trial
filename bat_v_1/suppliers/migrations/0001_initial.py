# Generated by Django 2.1.4 on 2019-01-09 10:29

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='suppliers.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Supplier Name')),
                ('alternate_name', models.CharField(blank=True, max_length=200, verbose_name='Supplier Alternative Name')),
                ('logo', models.ImageField(blank=True, upload_to='suppliers/logo/')),
                ('address1', models.CharField(blank=True, max_length=200)),
                ('address2', models.CharField(blank=True, max_length=200)),
                ('city', models.CharField(blank=True, max_length=200)),
                ('zip', models.CharField(blank=True, max_length=200, verbose_name='Zip/Pin Code')),
                ('region', models.CharField(blank=True, max_length=200, verbose_name='Region/State')),
                ('country', models.CharField(blank=True, max_length=200)),
                ('detail', models.TextField(blank=True)),
                ('create_date', models.DateTimeField(default=datetime.datetime(2019, 1, 9, 10, 29, 53, 237499, tzinfo=utc))),
                ('update_date', models.DateTimeField(default=datetime.datetime(2019, 1, 9, 10, 29, 53, 237517, tzinfo=utc))),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suppliers.Category', verbose_name='Select Category')),
            ],
        ),
    ]
