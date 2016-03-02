from django.shortcuts import *
from rotas_app.forms import *


def estabelecimento_cadastro(request):
    if request.method == 'POST':
        form  = FORMestabelecimento(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = FORMestabelecimento()
    return render_to_response("paginas_do_sistema/registra_estabelecimento.html" ,{"form":form}, context_instance = RequestContext(request))

def define_rota(request):
    if request.method == "POST":
        form = FORMrota(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = FORMrota()
    return render_to_response("paginas_da_rota/criar_rota.html",{"form":form}, context_instance = RequestContext(request))