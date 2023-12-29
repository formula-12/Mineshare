# Generated by Django 3.2.13 on 2023-12-29 03:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0007_auto_20231228_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servers',
            name='boost_regdate',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 28, 22, 15, 19, 471326), verbose_name='Дата регистрации CloudBoost-статуса'),
        ),
        migrations.AlterField(
            model_name='servers',
            name='premium_regdate',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 28, 22, 15, 19, 471326), verbose_name='Дата регистрации премиум-статуса'),
        ),
    ]
