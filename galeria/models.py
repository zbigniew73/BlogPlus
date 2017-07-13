# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.db.models import permalink

from blogplus.fields import ThumbnailImageField

class Galeria(models.Model):
	name=models.CharField(max_length=250, verbose_name=u'Nazwa')
	pub_date = models.DateTimeField(default=timezone.now, verbose_name=u'Data')
	description=models.TextField(verbose_name=u'Opis')

	class Meta:
		ordering=['name']

	def __str__(self):
		return self.name

	@permalink
	def get_absolute_url(self):
		return ('galeria_detail',None,{'pk':self.id})

class Foto(models.Model):
	galeria=models.ForeignKey(Galeria)
	title=models.CharField(max_length=100, verbose_name=u'Tytuł')
	image=ThumbnailImageField(upload_to='foto')
	caption=models.CharField(max_length=250,blank=True, verbose_name=u'Podpis')

	class Meta:
		ordering=['title']

	def __str__(self):
		return self.title

	@permalink
	def get_absolute_url(self):
		return ('foto_detail',None,{'pk':self.id})
