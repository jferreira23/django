from django.shortcuts import render
from django.http import HttpResponse
from perfis.models import Perfil

def index(request):
	return render(request, 'index.html')

def exibir(request, perfil_id):
	print 'ID do perfil recebido: %s' % (perfil_id)

	perfil = Perfil()

	if perfil_id == '1':
		perfil = Perfil('Jess', 'jess@mail.com', '12121212', 'MyCompany')

	return render(request, 'perfil.html', {"perfil":perfil})
