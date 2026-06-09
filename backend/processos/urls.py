from django.urls import path
from . import views

urlpatterns = [
    path('processos/', views.listar_registrar_processos),
    path('processos/<int:id>/atualizar/', views.atualizar_processo),
    path('processos/<int:id>/remover/', views.remover_processo),
    path('processos/advogado/<int:advogado_id>/', views.listar_processos_por_advogado),
    path('processos/<int:id>/', views.buscar_processo_por_id),
    path('processos/status/<str:status>/', views.listar_processos_por_status),
    path('processos/prioridade/<str:prioridade>/', views.listar_processos_por_prioridade),
]