from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre-nos/', views.sobre_nos, name='sobre_nos'),
    path('locais-disponiveis/', views.locais_disponiveis, name='locais_disponiveis'),
    path('corretores/', views.corretores, name='corretores'),
    path('contato/', views.contato, name='contato'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
]
