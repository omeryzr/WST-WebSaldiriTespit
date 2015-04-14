__author__ = 'omr24'
from django.conf.urls import patterns, include, url


urlpatterns = patterns('kontrolpaneli.views',
    url(r'^uyekayit', 'kayit_ekle'),


)
