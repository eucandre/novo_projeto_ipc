from django.shortcuts import *
from django.contrib.auth.decorators import login_required
from ipc_novo_app.forms import *


def acesso(request):

    return render_to_response("paginas_do_sistema/login.html")

#@login_required()
def pagina_inicial(request):
    return render_to_response("paginas_do_sistema/pagina_apresentacao.html")

def registra_grupos(request):
    if request.method == "post":
        form = FormSubgrupo(request.FILES, request.POST)
        if form.is_valid():
            form.save()
    else:
        form = FormSubgrupo()
    return render_to_response("paginas_do_sistema/subgrupos.html",{"form":form}, context_instance = RequestContext(request))
