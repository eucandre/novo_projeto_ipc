from django.shortcuts import *
from perfis.forms import *

def perfil_pesquisador(request):
    if request.method == "post":
        form = FormPerfil(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = FormPerfil()
    return render_to_response("paginas_perfis/registra_perfil.html",{"form":form}, context_instance = RequestContext(request))
