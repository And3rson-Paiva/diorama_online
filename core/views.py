from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
#from braces.views import GroupRequiredMixin
from .models import Arquivos, Empresas, Eventos
from django.core.paginator import Paginator, InvalidPage
from .forms import ContatoForm
from django import template
from django.contrib.auth.models import User
#from django.contrib.auth.forms import UserChangeForm


class CalendarioView(ListView):
    model = Eventos
    template_name = 'calendario_teste.html'

    def get_queryset(self):
        queryset = self.model.objects.filter(estado=True, usuario=self.request.user)
        return queryset


class FaturasView(TemplateView):
    template_name = 'faturas.html'


class ParceriaView(TemplateView):
    template_name = 'parceiros.html'


class IndexView(ListView):
    model = Arquivos
    template_name = 'index.html'

    def get_queryset(self):
        self.object_list = Arquivos.objects.count()
        return self.object_list


def contato(request):
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_email()

            messages.success(request, 'E-mail enviado com sucesso!')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar e-mail')
    context = {
        'form': form
    }
    return render(request, 'inbox.html', context)


class MinhaContaView(LoginRequiredMixin, ListView):
    model = Empresas
    login_url = reverse_lazy('url-login')
    template_name = 'minha-conta.html'

    def get_queryset(self):
        self.object_list = Empresas.objects.filter(usuario=self.request.user)
        return self.object_list


class LoginView(TemplateView):
    template_name = 'login.html'


############ LISTA ###################
class ArquivoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('url-login')
    model = Arquivos
    template_name = 'documentos.html'
    paginate_by = 4

    def get_queryset(self):
        self.object_list = Arquivos.objects.filter(usuario=self.request.user)
        return self.object_list


class IndexList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('url-login')
    model = Arquivos
    template_name = 'lista.html'


###################### CLASSES CREATE ###############################
class ArquivosCreate(CreateView):
    model = Arquivos
    fields = ['titulo', 'empresa', 'data_envio', 'descricao', 'categorias', 'arquivo']
    template_name = 'enviar_arquivo.html'
    success_url = reverse_lazy('url-documentos')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url


###################### CLASSE DELETE ###############################
class ArquivosDelete(DeleteView):
    model = Arquivos
    template_name = 'minha-empresa.html'
    success_url = reverse_lazy('url-documentos')

    def get_queryset(self):
        self.object_list = Arquivos.objects.filter(usuario=self.request.user)
        return self.object_list


def submit_login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            django_login(request, user)
            return redirect('url-index')
        else:
            messages.error(request, 'Usuário/Senha inválidos, tente novamente')
            return redirect('url-login')


def logout(request):
    django_logout(request)
    return redirect('url-login')


class ExtraView(TemplateView):
    login_url = reverse_lazy('url-login')
    template_name = 'extras.html'
