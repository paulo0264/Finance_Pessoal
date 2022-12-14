# Generated by Django 4.1.4 on 2022-12-13 17:53

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=70, verbose_name='usuario')),
                ('email', models.EmailField(db_index=True, max_length=70, unique=True, verbose_name='email')),
                ('is_active', models.BooleanField(default=False, help_text='Se ativo o usuário tem permissão para acessar o sistema', verbose_name='ativo')),
                ('tipo', models.CharField(choices=[('ADMINISTRADOR', 'Administrador'), ('COMUM', 'Comum')], default='COMUM', max_length=15, verbose_name='tipo do usuário')),
            ],
            options={
                'verbose_name': 'usuário',
                'verbose_name_plural': 'usuários',
                'ordering': ['username'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
