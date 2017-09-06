# novo arquivo connectedin/perfis/urls.py

from django.conf.urls import patterns, url
from perfis import views.index

urlpatterns = patterns('',
    url(r'^$', index, 'perfis.views.index')
)
