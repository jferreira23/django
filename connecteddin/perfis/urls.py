from django.conf.urls import patterns, url
#from perfis import views

urlpatterns = patterns('',
	url(r'^$', 'perfis.views.index', name="index"),
	#url(r'^$', index, name='index')
	url(r'^perfis/(?P<perfil_id>\d+)$', 'perfis.views.exibir', name="exibir"),
	url(r'^perfis/(?P<perfil_id>\d+)/convidar$', 'perfis.views.convidar', name="convidar"),
	url(r'^convite/(?P<convite_id>\d+)/aceitar', 'perfis.views.aceitar', name='aceitar')
)
