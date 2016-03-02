from perfis.models import *
from django import forms

class FormPerfil(forms.ModelForm):
    Nome_pesquisador = forms.CharField(label="Nome do pesquisador",max_length=150,widget=forms.TextInput(attrs={"class":"form-control","required":"required"}))

    class Meta:
       model = perfil
       fields = ("Nome_pesquisador",)

