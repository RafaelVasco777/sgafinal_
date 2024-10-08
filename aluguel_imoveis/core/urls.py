from django.urls import path
from .views import (
    imovel_list, imovel_create, imovel_update, imovel_delete,
    proprietario_list, proprietario_create, proprietario_update, proprietario_delete,
    cliente_list, cliente_create, cliente_update, cliente_delete,
    contrato_list, contrato_create, contrato_update, contrato_delete,
    pagamento_list, pagamento_create, pagamento_update, pagamento_delete,
)

urlpatterns = [
    path('', imovel_list, name='imovel_list'),
    path('imovel/create/', imovel_create, name='imovel_create'),
    path('imovel/<int:pk>/update/', imovel_update, name='imovel_update'),
    path('imovel/<int:pk>/delete/', imovel_delete, name='imovel_delete'),

    path('proprietario/', proprietario_list, name='proprietario_list'),
    path('proprietario/create/', proprietario_create, name='proprietario_create'),
    path('proprietario/<int:pk>/update/', proprietario_update, name='proprietario_update'),
    path('proprietario/<int:pk>/delete/', proprietario_delete, name='proprietario_delete'),

    path('cliente/', cliente_list, name='cliente_list'),
    path('cliente/create/', cliente_create, name='cliente_create'),
    path('cliente/<int:pk>/update/', cliente_update, name='cliente_update'),
    path('cliente/<int:pk>/delete/', cliente_delete, name='cliente_delete'),

    path('contrato/', contrato_list, name='contrato_list'),
    path('contrato/create/', contrato_create, name='contrato_create'),
    path('contrato/<int:pk>/update/', contrato_update, name='contrato_update'),
    path('contrato/<int:pk>/delete/', contrato_delete, name='contrato_delete'),

    path('pagamento/', pagamento_list, name='pagamento_list'),
    path('pagamento/create/', pagamento_create, name='pagamento_create'),
    path('pagamento/<int:pk>/update/', pagamento_update, name='pagamento_update'),
    path('pagamento/<int:pk>/delete/', pagamento_delete, name='pagamento_delete'),
]