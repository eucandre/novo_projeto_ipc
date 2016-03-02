"""novo_projeto_ipc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import patterns, include, url
from django.conf import settings


from ipc_novo_app.views import *
from rotas_app.views import *
from perfis.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$','ipc_novo_app.views.pagina_inicial'),
    url(r'^sub_produtos/$','ipc_novo_app.views.registra_grupos'),
    url(r'^pesos_grupo/$','ipc_novo_app.views.pesos_grupos'),
    url(r'^reg_item/$','ipc_novo_app.views.registra_itens'),
    url(r'^pesos_item/$','ipc_novo_app.views.pesos_subitens'),

    #--------- rotas ---------------
    url(r'^estabelecimento/$','rotas_app.views.estabelecimento_cadastro'),
    url(r'^rota/$','rotas_app.views.define_rota'),
    url(r'^perfil/$','perfis.views.perfil_pesquisador'),
    url(r'^login/$',"django.contrib.auth.views.login",{"template_name":"paginas_do_sistema/login.html"}),
    url(r'^logout/$',"django.contrib.auth.views.logout_then_login",{"login_url":"/login/"}),


]
urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }))
