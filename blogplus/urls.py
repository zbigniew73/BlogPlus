"""blogplus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.views.generic.base import TemplateView
from django.contrib import admin
from blogplus.views import markdown_uploader
from fotogaleria import views
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Blog URLs
    url(r'', include('blog.urls', namespace="blog")),

    # Galeria URLs
    url(r'^galeria/', include('galeria.urls')),
    url(r'^photo/$', views.photo_galeria, name='photo_galeria'),
    # Draceditor
    url(r'^draceditor/', include('draceditor.urls')),
    url(r'^api/uploader/$', markdown_uploader, name='markdown_uploader_page'),

    # Flat pages
    url(r'', include('django.contrib.flatpages.urls')),

    # Robots.txt Humans.txt
    url(r'^robots\.txt/$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    url(r'^humans\.txt/$', TemplateView.as_view(template_name='humans.txt', content_type='text/plain')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
