from rotas_app.models import *
from django import forms

class FORMestabelecimento(forms.ModelForm):
    
    class Meta:
        model = estabelecimento
        fields = ['NomeDoEstabeleciemento','Bairro','Rua','TeleFone','Email',]

class FORMrota(forms.ModelForm):

    data_vizita = forms.DateField(widget=forms.widgets.DateInput(format="%m/%d/%Y", attrs={"class":"form-control"}))
    Local_vizitar = forms.ModelChoiceField(queryset=estabelecimento.objects.all(),widget=forms.Select(attrs={"class":"form-control","required":"required"}))
    Pesquisador =forms.ModelChoiceField(queryset=perfil.objects.all(),widget=forms.Select(attrs={"class":"form-control","required":"required"}))
    grupo_para_pesquisa = forms.ModelChoiceField(label="Grupo para ser pesquisado", queryset=pesos_grupos.objects.all(),widget=forms.Select(attrs={"class":"form-control","required":"required"}))
    SubGrupoParaPesquisa= forms.ModelChoiceField(label="Sub-grupo para ser pesquisado",queryset=subgrupo.objects.all(),widget=forms.Select(attrs={"class":"form-control","required":"required"}))
    Item_pesquisado = forms.ModelChoiceField(label="Item para ser pesquisado",queryset=item.objects.all(),widget=forms.Select(attrs={"class":"form-control","required":"required"}))

    class Meta:
        model = rota
        fields =['data_vizita','Local_vizitar','Pesquisador','grupo_para_pesquisa','SubGrupoParaPesquisa','Item_pesquisado',]









