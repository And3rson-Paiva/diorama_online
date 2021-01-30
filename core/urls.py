from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import IndexView, contato, MinhaContaView
from core.views import submit_login, logout
from .views import ArquivoList, ArquivosDelete, ArquivosCreate, IndexList, ExtraView, ParceriaView, FaturasView, CalendarioView
from . import views

urlpatterns = [
    path('', login_required(IndexView.as_view()), name='url-index'),

    path('login/submit', submit_login, name='submit_login'),
    path('logout/', logout, name='url-logout'),

    path('contato/', contato, name='url-contato'),
    path('faturas/', FaturasView.as_view(), name='url-faturas'),
    path('calendario/', CalendarioView.as_view(), name='url-calendario'),

    path('documentos/', ArquivoList.as_view(), name='url-documentos'),
    path('lista/arquivos/', IndexList.as_view(), name='url-lista'),

    path('minha-conta/', MinhaContaView.as_view(), name='url-minha-conta'),
    path('parceiros/', ParceriaView.as_view(), name='url-parceiros'),
    path('extras/', ExtraView.as_view(), name='url-extra'),
    path('arquivos/novo/', ArquivosCreate.as_view(), name='url-arquivo-novo'),

    path('excluir/arquivos/<int:pk>/', views.ArquivosDelete.as_view(), name='url-delete-arquivos'),
]

