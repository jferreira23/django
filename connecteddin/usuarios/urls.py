from django.conf.urls import patterns, url
from views import RegistrarUsuariosView

urlpatterns = patterns('',
    url(r'^registrar/$', RegistrarUsuariosView.as_view(), name="registrar")
    )