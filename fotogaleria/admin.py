# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Photo


@admin.register(Photo)
class PhotoGaleriaAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp', 'width', 'height')
    exclude = ('width', 'height')
    list_display_links = ('title', 'timestamp')

    class Meta:
        model = Photo
