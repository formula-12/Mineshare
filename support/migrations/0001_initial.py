# Generated by Django 4.0 on 2022-12-04 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Support',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_from_user', models.TextField(default='Anonimous')),
                ('email', models.TextField()),
                ('text', models.TextField()),
                ('completed', models.BooleanField(default=False)),
                ('name_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='Отправитель')),
            ],
            options={
                'verbose_name_plural': 'Обращения',
            },
        ),
    ]
