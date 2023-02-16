from django.contrib import admin
from django.urls import path, include
from funcionarios import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('atendimento/', include('funcionarios.urls')),

]
