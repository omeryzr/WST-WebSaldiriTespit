__author__ = 'omr24'
from django.conf.urls import patterns, include, url
import monitoring.views

urlpatterns = patterns('monitoring.views',
    url(r'^index', 'anasayfa'),
    url(r'^saldirilar', 'saldiri'),
    url(r'^sqlinjection', 'sqlsaldiri'),
    url(r'^xss', monitoring.views.xsssaldiri),
    url(r'^urlgiris', monitoring.views.urlgiris),
    url(r'^iletisim', 'iletisimsayfasi'),
    url(r'^profil', 'profilsayfasi'),
    url(r'^uyeol', 'kayit_ekle')


)
