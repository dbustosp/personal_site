from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    
    url(r'^$', 'web.views.index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/', 'web.views.index'),
)
