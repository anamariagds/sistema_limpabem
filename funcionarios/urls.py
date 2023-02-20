from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('validando_acesso/', views.validando_acesso, name="validando_acesso"),
    path('sair/', views.sair, name="sair")
]