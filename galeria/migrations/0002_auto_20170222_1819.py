# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2017-02-22 17:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foto',
            name='caption',
            field=models.CharField(blank=True, max_length=250, verbose_name='Podpis'),
        ),
        migrations.AlterField(
            model_name='foto',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Tytuł'),
        ),
        migrations.AlterField(
            model_name='galeria',
            name='description',
            field=models.TextField(verbose_name='Opis'),
        ),
        migrations.AlterField(
            model_name='galeria',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Nazwa'),
        ),
    ]
