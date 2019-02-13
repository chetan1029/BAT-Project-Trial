# Generated by Django 2.1.4 on 2019-02-12 12:50

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0082_auto_20190212_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aql',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 12, 50, 47, 148165, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aql',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 12, 50, 47, 148181, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bank',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 12, 50, 47, 144028, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bank',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 12, 50, 47, 144046, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='certification',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 12, 50, 47, 151427, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='certification',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 12, 50, 47, 151445, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 12, 50, 47, 143388, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 12, 50, 47, 143409, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contract',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 12, 50, 47, 145043, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contract',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 12, 50, 47, 145060, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='mold',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 12, 50, 47, 146105, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='mold',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 12, 50, 47, 146121, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='moldfile',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 12, 50, 47, 147241, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='moldfile',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 12, 50, 47, 147258, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='moldhost',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 12, 50, 47, 147675, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='moldhost',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 12, 50, 47, 147691, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 12, 50, 47, 148734, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='currency',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.PROTECT, to='settings.Currency', verbose_name='Select Currency'),
        ),
        migrations.AlterField(
            model_name='order',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 12, 50, 47, 148751, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderdelivery',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 12, 50, 47, 150918, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderdelivery',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 12, 50, 47, 150935, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderfile',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 12, 50, 47, 149819, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderfile',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 12, 50, 47, 149836, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderpayment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 12, 50, 47, 150281, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderpayment',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 12, 50, 47, 150299, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 12, 50, 47, 149345, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 12, 50, 47, 149362, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='paymentterms',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 12, 50, 47, 141988, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='paymentterms',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 12, 50, 47, 142005, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='productprice',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 12, 50, 47, 145521, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='productprice',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 12, 50, 47, 145537, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 12, 50, 47, 142472, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 12, 50, 47, 142492, tzinfo=utc)),
        ),
    ]
