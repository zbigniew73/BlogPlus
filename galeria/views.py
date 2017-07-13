# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views import generic
from galeria.models import Galeria, Foto
        
class IndexView(generic.ListView):
    template_name = 'galeria/index.html'
    def get_queryset(self):
        return Galeria.objects.all()[:5]
        
class ListView(generic.ListView):
    model = Galeria
    template_name = 'galeria/galeria_list.html'
        
class GaleriaDetailView(generic.DetailView):
    model = Galeria
    template_name = 'galeria/galeria_detail.html'
        
class FotoDetailView(generic.DetailView):
    model = Foto
    template_name = 'galeria/foto_detail.html'
