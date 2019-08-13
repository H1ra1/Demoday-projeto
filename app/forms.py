from django import forms
from app.models import Cadastro

class CadastroForm (forms.ModelForm):
    class Meta:
        model = Cadastro
        fields = [
            'Nome Completo'
            'Nome de usuário'
            'E-mail'
            'Celular'
            'Senha'
            'Foto'
        ]
        widgets = {
            'Senha': forms.PasswordInput(),
        }

class EntrarForm(forms.Form):
    nome_usuario = forms.CharField(max_length=40, widget= forms.TextInput(attrs={'placeholder': 'Digite seu usuário'}))
    senha = forms.CharField(max_length=10, widget= forms.PasswordInput(attrs={'placeholder': 'Digite sua senha'}))