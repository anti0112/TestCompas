# Generated by Django 3.2.13 on 2022-07-06 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('role', models.CharField(choices=[('u', 'Пользователь'), ('m', 'Менеджер'), ('a', 'CRM-администратор')], max_length=255, verbose_name='Место работы')),
                ('avatar', models.ImageField(upload_to='app/user_selection/static/img')),
                ('offer', models.BooleanField(default=None)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]