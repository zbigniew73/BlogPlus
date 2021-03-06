# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2017-02-24 17:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=60, verbose_name='Tytuł')),
                ('description', models.TextField(blank=True, default='', max_length=200, verbose_name='Opis')),
                ('width', models.IntegerField(default=0, verbose_name='Szerokość')),
                ('height', models.IntegerField(default=0, verbose_name='Wysykość')),
                ('image', models.ImageField(height_field='height', upload_to='', verbose_name='Obraz', width_field='width')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Data')),
            ],
        ),
    ]
