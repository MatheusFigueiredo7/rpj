import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Advogado

@csrf_exempt
def buscar_advogado_por_id(request, id):
    if request.method == 'GET':
        try:
            advogado = Advogado.objects.values().get(id=id)
            return JsonResponse(advogado)
        except Advogado.DoesNotExist:
            return JsonResponse({'erro': 'Advogado não encontrado.'}, status=404)

@csrf_exempt
def listar_advogados_ativos(request):
    if request.method == 'GET':
        advogados = list(Advogado.objects.filter(ativo=True).values())
        if not advogados:
            return JsonResponse({'mensagem': 'Nenhum advogado ativo encontrado.'}, status=404)
        return JsonResponse(advogados, safe=False)

@csrf_exempt
def listar_registrar_advogados(request):
    if request.method == 'GET':
        advogados = list(Advogado.objects.all().values())
        return JsonResponse(advogados, safe=False)

    elif request.method == 'POST':
        dados = json.loads(request.body)
        
        novo_advogado = Advogado.objects.create(
            nome=dados['nome'],
            oab=dados['oab'],
            ativo=dados.get('ativo', True)
        )
        
        return JsonResponse({
            'id': novo_advogado.id, 
            'mensagem': 'Advogado registrado com sucesso!'
        }, status=201)