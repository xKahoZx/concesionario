from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'concesionario.views.home', name='home'),
    # url(r'^concesionario/', include('concesionario.foo.urls')),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root:settings.MEDIA_ROOT'}),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^',include('concesionario.apps.ventas.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
