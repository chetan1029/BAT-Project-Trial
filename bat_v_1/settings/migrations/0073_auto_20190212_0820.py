# Generated by Django 2.1.4 on 2019-02-12 08:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0072_auto_20190212_0816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amazonmarket',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 8, 20, 8, 715221, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='amazonmarket',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 8, 20, 8, 715237, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='amazonmwsauth',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 8, 20, 8, 715599, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='amazonmwsauth',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 8, 20, 8, 715616, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='box',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 8, 20, 8, 714832, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='box',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 8, 20, 8, 714862, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='currency',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 8, 20, 8, 714385, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='currency',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 8, 20, 8, 714405, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='status',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 8, 20, 8, 713988, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='status',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 12, 8, 20, 8, 714019, tzinfo=utc)),
        ),
    ]
