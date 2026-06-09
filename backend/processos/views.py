import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Processo

@csrf_exempt
def buscar_processo_por_id(request, id):
    if request.method == 'GET':
        try:
            processo = Processo.objects.values().get(id=id)
            return JsonResponse(processo)
        except Processo.DoesNotExist:
            return JsonResponse({'erro': 'Processo não encontrado.'}, status=404)

@csrf_exempt
def listar_processos_por_status(request, status):
    if request.method == 'GET':
        processos = list(Processo.objects.filter(status=status.upper()).values())
        if not processos:
            return JsonResponse({'mensagem': f'Nenhum processo com status {status.upper()} encontrado.'}, status=404)
        return JsonResponse(processos, safe=False)

@csrf_exempt
def listar_processos_por_prioridade(request, prioridade):
    if request.method == 'GET':
        processos = list(Processo.objects.filter(prioridade=prioridade.upper()).values())
        if not processos:
            return JsonResponse({'mensagem': f'Nenhum processo com prioridade {prioridade.upper()} encontrado.'}, status=404)
        return JsonResponse(processos, safe=False)

@csrf_exempt
def listar_processos_por_advogado(request, advogado_id):
    if request.method == 'GET':
        processos = list(Processo.objects.filter(advogado_responsavel_id=advogado_id).values())
        
        if not processos:
            return JsonResponse({'mensagem': 'Nenhum processo encontrado para este advogado.'}, status=404)
            
        return JsonResponse(processos, safe=False)

@csrf_exempt
def listar_registrar_processos(request):
    if request.method == 'GET':
        processos = list(Processo.objects.all().values())
        return JsonResponse(processos, safe=False)

    elif request.method == 'POST':
        dados = json.loads(request.body)
        
        novo_processo = Processo.objects.create(
            numero_processo=dados['numero_processo'],
            descricao=dados['descricao'],
            status=dados.get('status', 'ABERTO'),
            prioridade=dados.get('prioridade', 'NAO_URGENTE'),
            advogado_responsavel_id=dados.get('advogado_responsavel_id') 
        )
        
        return JsonResponse({
            'id': novo_processo.id, 
            'numero_processo': novo_processo.numero_processo,
            'mensagem': 'Processo registrado com sucesso!'
        }, status=201)
        
@csrf_exempt
def atualizar_processo(request, id):
    if request.method == 'PUT':
        try:
            processo = Processo.objects.get(id=id)
            dados = json.loads(request.body)
            
            if 'status' in dados:
                processo.status = dados['status']
            if 'prioridade' in dados:
                processo.prioridade = dados['prioridade']
            
            processo.save()
            
            return JsonResponse({'mensagem': f'Processo atualizado com sucesso!'})
        
        except Processo.DoesNotExist:
            return JsonResponse({'erro': 'Processo não encontrado.'}, status=404)

@csrf_exempt
def remover_processo(request, id):
    if request.method == 'DELETE':
        try:
            processo = Processo.objects.get(id=id)
            processo.delete()
            
            return JsonResponse({'mensagem': 'Processo removido com sucesso!'})
            
        except Processo.DoesNotExist:
            return JsonResponse({'erro': 'Processo não encontrado.'}, status=404)