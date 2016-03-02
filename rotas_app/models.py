from __future__ import unicode_literals

from django.db import models
from ipc_novo_app.models import *
from perfis.models import *
from ipc_novo_app.models import *

class estabelecimento(models.Model):
    NomeDoEstabeleciemento = models.CharField(max_length=150)
    Bairro = models.CharField(max_length=150)
    Rua = models.CharField(max_length=150)
    TeleFone = models.CharField(max_length=150, blank=True)
    Email = models.EmailField(blank=True)
    #usuario = models.ForeignKey(User)

    def __unicode__(self):
        return self.NomeDoEstabeleciemento
    class Meta:
        verbose_name_plural = "Estabelecimento"


class rota(models.Model):
    Local_vizitar        = models.ForeignKey(estabelecimento)
    Pesquisador          = models.ForeignKey(perfil)
    data_vizita          = models.DateField()
    grupo_para_pesquisa  = models.ForeignKey(pesos_grupos)
    SubGrupoParaPesquisa = models.ForeignKey(subgrupo)
    Item_pesquisado      = models.ForeignKey(item)
    #usuario              = models.ForeignKey(User)

    def __unicode__(self):
        return self.Local_vizitar

    class Meta:
        verbose_name_plural = "Rota da pesquisa"

