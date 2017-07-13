# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Galeria, Foto

class FotoInline(admin.StackedInline):
    model=Foto

class GaleriaAdmin(admin.ModelAdmin):
    inlines=[FotoInline]

admin.site.register(Galeria, GaleriaAdmin)
admin.site.register(Foto)
