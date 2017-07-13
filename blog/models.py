# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from taggit.managers import TaggableManager
from django.utils.text import slugify
from django.utils import timezone
from draceditor.models import DraceditorField
from django.db.models.signals import post_save
from django.core.cache import cache

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name=u'Tytuł')
    image = models.ImageField(
            upload_to='post',
            null=True,
            blank=True,
            width_field = "width_field",
            height_field = "height_field", verbose_name=u'Foto Image')
    height_field = models.IntegerField(default=0, verbose_name=u'Wysokość')
    width_field = models.IntegerField(default=0, verbose_name=u'Szerokość')
    pub_date = models.DateTimeField(default=timezone.now, verbose_name=u'Data')
    text = DraceditorField(verbose_name=u'Treść')
    slug = models.SlugField(max_length=40, unique=True, verbose_name=u'Odnośnik')
    author = models.ForeignKey(User, verbose_name=u'Autor')
    site = models.ForeignKey(Site, verbose_name=u'Strona')
    tags = TaggableManager(verbose_name=u'Tag')    


    def get_absolute_url(self):
        return "/%s/%s/%s.html" % (self.pub_date.year, self.pub_date.month, self.slug)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-pub_date"]

# Define signals
def new_post(sender, instance, created, **kwargs):
    cache.clear()

# Set up signals
post_save.connect(new_post, sender=Post)
