# -*- coding: utf-8 -*-
from django.conf.urls import url
from galeria import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^list/$', views.ListView.as_view(), name='galeria_list'),
    url(r'^(?P<pk>\d+)/$', views.GaleriaDetailView.as_view(), name='galeria_detail'),
    url(r'^foto/(?P<pk>\d+)/$', views.FotoDetailView.as_view(), name='foto_detail'),
]
