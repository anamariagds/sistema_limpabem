from django.urls import path
from . import views

urlpatterns = [
    path('ver_atendimentos/', views.ver_atendimentos, name="ver_atendimentos"),
    path('novo_atendimento/', views.novo_atendimento, name="novo_atendimento"),
    path('atendimento_detalhes/<int:id>/', views.atendimento_detalhes, name="atendimento_detalhes"),
    path('atualizar_status/<int:id_atendimento>/', views.atualizar_status, name="atualizar_status"),



]