from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from .models import Usuario, Produto, Pedido
import json


@csrf_exempt
def index(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            Usuario.objects.create(nome=data['nome'], cpf=data['cpf'])
        except IntegrityError:
            return JsonResponse({'Erro': 'Já existe um usuário com este CPF!'},
                                json_dumps_params={'ensure_ascii': False})
    return JsonResponse({'Menssagem': 'Cadastrado com Sucesso'})


@csrf_exempt
def produto(request):
    if request.method == 'GET':
        produto = list(Produto.objects.values())
        return JsonResponse(produto, safe=False)

    if request.method == 'POST':
        data = json.loads(request.body)
        pedido = Pedido.objects.create(
            quantidade=data['quantidade'],
            valor_total=data['valor_total'],
            status=data['status']
        )
        return JsonResponse('')
