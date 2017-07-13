# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import ListView, DetailView
from blog.models import Post
from taggit.models import Tag
from blog.views import TagListView, PostsFeed, AtomPostsFeed, getSearchResults
from django.contrib.sitemaps.views import sitemap
from blog.sitemap import PostSitemap, GaleriaSitemap, FlatpageSitemap

# Define sitemaps
sitemaps = {
    'posts': PostSitemap,
    'galeria': GaleriaSitemap,
    'pages': FlatpageSitemap
}

urlpatterns = [
    # Index
    url(r'^(?P<page>\d+)?/?$', ListView.as_view(
        model=Post,
        paginate_by=5,
        ),
        name='index'
        ),

    # Individual posts
    url(r'^(?P<pub_date__year>\d{4})/(?P<pub_date__month>\d{1,2})/(?P<slug>[a-zA-Z0-9-]+).html?$', DetailView.as_view(
        model=Post,
        ),
        name='post'
        ),

    # Tags
    url(r'^tag/(?P<slug>[a-zA-Z0-9-]+).html?$', TagListView.as_view(
        paginate_by=5,
        model=Tag,
        ),
        name='tag'
        ),

    # Post RSS feed
    url(r'^feeds/posts/$', PostsFeed()),

    # Post RSS Atom
    url(r'^atom/posts/$', AtomPostsFeed()),

    # Search posts
    url(r'^search', getSearchResults, name='search'),

    # Sitemap
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
            name='django.contrib.sitemaps.views.sitemap'),
]
