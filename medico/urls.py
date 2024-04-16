from django.urls import path, include
from . import views

urlpatterns = [
    path('cadastro_medico/', views.cadastro_medico, name='cadastro_medico'),
]