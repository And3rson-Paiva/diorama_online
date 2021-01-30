from django.contrib import admin
from .models import Empresas, Arquivos, Eventos
from .forms import EventoForm

class EventoAdmin(admin.ModelAdmin):
    form = EventoForm
    list_display = ('usuario', 'empresa', 'inicio', 'vencimento', 'estado')



admin.site.register(Eventos, EventoAdmin)




@admin.register(Empresas)
class EmpresasAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'cnpj', 'razao_social', 'nome_fantasia', 'cnae', 'logradouro', 'numero', 'estado', 'cidade', 'complemento', 'cep', 'inscricao_estadual', 'inscricao_municipal')


@admin.register(Arquivos)
class ArquivosAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'usuario', 'titulo', 'descricao', 'data_envio', 'arquivo', 'categorias')






"""
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'cpf', 'cidade', 'email', 'fone', 'imagem', 'arq', 'criado', 'modificado', 'ativo')
    exclude = ('nome',)

    def _nome(self, instance):
        return f'{instance.nome.get_full_name()}'

    def get_queryset(self, request):
        qs = super(ClienteAdmin, self).get_queryset(request)
        return qs.filter(nome=request.user)

    def save_model(self, request, obj, form, change):
        obj.nome = request.user
        super().save_model(request, obj, form, change)
"""
