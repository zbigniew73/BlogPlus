# -*- coding: utf-8 -*-
from django.db import models

class Photo(models.Model):
    title = models.CharField(max_length=60, default='', blank=True, verbose_name=u'Tytuł')
    description = models.TextField(max_length=200, default='', blank=True, verbose_name=u'Opis')
    width = models.IntegerField(default=0, verbose_name=u'Szerokość')
    height = models.IntegerField(default=0, verbose_name=u'Wysykość')
    image = models.ImageField(width_field="width", height_field="height" , verbose_name=u'Obraz')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name=u'Data')

def __str__(self):
        return self.title

class Meta:
        ordering = ["timestamp"]
        verbose_name = 'Obraz'
