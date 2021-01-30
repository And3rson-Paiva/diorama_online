from django import forms
from django.core.mail.message import EmailMessage
from .models import Eventos, Empresas
#from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class EventoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields['empresa'].queryset = Empresas.objects.filter(estado=True, )

    class Meta:
        model = Eventos
        fields = '__all__'


# Para envio de email
class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=120)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_email(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'

        mail = EmailMessage(
            subject='E-mail enviado pelo sistema Diorama',
            body=conteudo,
            from_email='and3rsonpaiva@gmail.com',
            to=['and3rsonpaiva@gmail.com',],
            headers={'Reply-To': email}
        )
        mail.send()













"""
class CustomUsuarioCreateForm(UserCreationForm):
    class Meta:
        model = CustomUsuario
        fields = ('first_name', 'last_name')
        labels = {'username': 'Username/E-mail'}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.email = self.cleaned_data['username']
        if commit:
            user.save()
        return user


class CustomUsuarioChangeForm(UserChangeForm):
    class Meta:
        model = CustomUsuario
        fields = ('first_name', 'last_name', 'fone')
"""


"""

class ContatoModelForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'imagem']


class ArquivoModelForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'imagem']


# Para envio de email
class ContatoForm(forms.Form):
    nome = forms.CharField(label='Primeiro nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=120)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_email(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'

        mail = EmailMessage(
            subject='E-mail enviado pelo sistema django2',
            body=conteudo,
            from_email='and3rsonpaiva@gmail.com',
            to=['and3rsonpaiva@gmail.com', ],
            headers={'Reply-To': email}
        )
        mail.send()


class ArquivoModelForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'imagem']
"""
