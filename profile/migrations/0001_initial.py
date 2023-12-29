# Generated by Django 4.2.8 on 2023-12-29 00:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ServersBuffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('server_ip', models.TextField(max_length=36, verbose_name='Адрес')),
                ('server_port', models.TextField(default='25565', max_length=5, verbose_name='Порт')),
                ('name', models.TextField(max_length=50, verbose_name='Название')),
                ('published', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Серверы на проверке',
            },
        ),
    ]