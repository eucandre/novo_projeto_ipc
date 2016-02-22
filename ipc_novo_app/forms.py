__author__ = 'Carlos'

from django import forms
from models import *

GRUPOS = ((u'Aliemntacao_e_bebidas','Aliemntacao_e_bebidas'),(u'Habitacao','Habitacao'),(u'Artigos_e_residencia','Artigos_e_residencia'),
(u'Vestuario','Vestuario'),(u'Transportes','Transportes'),(u'Saude_e_cuidados_especiais','Saude_e_cuidados_especiais'),
(u'Despesas_pessoais','Despesas_pessoais'),(u'Educacao','Educacao'),(u'Comunicacao','Comunicao'))




class FormPesos_grupos(forms.ModelForm):
    grupo = forms.ChoiceField(choices=GRUPOS, widget=forms.Select(attrs={"class":"form-control"}))
    peso = forms.FloatField(widget=forms.TextInput(attrs={"class":"form-control","mask": "99-999999"}))

    class Meta:
        model = pesos_grupos
        fields = ['grupo','peso']#,'usuario']

class FormSubgrupo(forms.ModelForm):
    grupo_relacionado = forms.ModelChoiceField(queryset=pesos_grupos.objects.all(),widget=forms.Select(attrs={"class":"form-control","required":"required"}))
    class Meta:
        model = subgrupo
        fields = ['nome_subgrupo', 'peso_subgrupo','grupo_relacionado']

class FormItem(forms.ModelForm):
    nome_item = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    class Meta:
        model = item
        fields = ['nome_item',]

class FormSubitem(forms.ModelForm):
    item_relacionado = forms.ModelChoiceField(queryset=item.objects.all(),widget=forms.Select(attrs={"class":"form-control","required":"required"}))
    class Meta:
        model = subitem
        fields = ['nome_subitem','peso_subitem','item_relacionado']