# -*- coding: utf-8 -*-
from django.contrib.sitemaps import Sitemap
from django.contrib.flatpages.models import FlatPage
from blog.models import Post
from galeria.models import Galeria

class PostSitemap(Sitemap):
    changefreq = "always"
    priority = 0.9

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.pub_date

class GaleriaSitemap(Sitemap):
    changefreq = "always"
    priority = 0.9

    def items(self):
        return Galeria.objects.all()

    def lastmod(self, obj):
        return obj.pub_date

class FlatpageSitemap(Sitemap):
    changefreq = "always"
    priority = 0.9

    def items(self):
        return FlatPage.objects.all()
