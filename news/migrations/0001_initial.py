# Generated by Django 4.0 on 2022-12-03 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=100, verbose_name='Заголовок')),
                ('description', models.TextField(blank=True, max_length=2000, verbose_name='Текст')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='Дата публикации')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='Владелец')),
            ],
            options={
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
