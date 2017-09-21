# arquivo onde as rotas sao configuradas
# novo arquivo connectedin/perfis/urls.py
from django.conf.urls import patterns, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'perfis.views.index'),
    url(r'^perfis$', 'perfis.views.exibir'),
)
