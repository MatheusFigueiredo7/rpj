from django.urls import path
from . import views

urlpatterns = [
    path('advogados/', views.listar_registrar_advogados),
    path('advogados/<int:id>/', views.buscar_advogado_por_id),
    path('advogados/ativos/', views.listar_advogados_ativos),
]