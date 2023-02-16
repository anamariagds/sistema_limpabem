from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name="login"),
    path('validando_acesso/', views.validando_acesso, name="validando_acesso"),
    path('sair/', views.sair, name="sair")
]