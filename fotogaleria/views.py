# -*- coding: utf-8 -*-
from django.shortcuts import render
from fotogaleria.models import Photo


def photo_galeria(request):
    queryset = Photo.objects.all()
    context = {
        "photos": queryset,
    }
    return render(request, 'photos.html', context)
