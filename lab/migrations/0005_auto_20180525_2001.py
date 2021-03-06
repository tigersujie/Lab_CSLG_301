# Generated by Django 2.0.5 on 2018-05-25 20:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0004_auto_20180517_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='last_modified_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 25, 20, 1, 37, 558171), verbose_name='修改时间'),
        ),
        migrations.AlterField(
            model_name='article',
            name='member',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lab.Member', verbose_name='作者'),
        ),
    ]
