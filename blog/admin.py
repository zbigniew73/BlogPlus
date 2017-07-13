# -*- coding: utf-8 -*-
from . import models
from django.contrib import admin
from django.contrib.auth.models import User
from draceditor.widgets import AdminDraceditorWidget

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "pub_date")
    prepopulated_fields = {"slug": ("title",)}
    exclude = ('author',)

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

admin.site.register(models.Post, PostAdmin)
admin.site.site_header = 'Administracja BlogPlus'
