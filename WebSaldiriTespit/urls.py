from django.conf.urls import patterns, include, url
from django.contrib import admin
import kontrolpaneli.views
import monitoring.views
import django.contrib.auth
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'WebSaldiriTespit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('kontrolpaneli.urls')),
    url(r'', include('monitoring.urls')),

    url(r'login/$','django.contrib.auth.views.login',
 		{'template_name':'login.html'}),
	url(r'logout/$','django.contrib.auth.views.logout',
		{'next_page':'/accounts/login/'}),

)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()