from django.db import models


class Usuario(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    cpf = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)
    valor = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nome


class Pedido(models.Model):
    ESPERA = 'ES'
    CANCELADO = 'CC'
    PAGO = 'PG'
    EM_PREPARO = 'EP'
    FINALIZADO = 'FN'
    PEDIDOS_CHOICE = [
        (ESPERA, 'ESPERA'),
        (CANCELADO, 'CANCELADO'),
        (PAGO, 'PAGO'),
        (EM_PREPARO, 'EM_PREPARO'),
        (FINALIZADO, 'FINALIZADO')
    ]
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    valor_total = models.PositiveIntegerField()
    status = models.CharField(max_length=2, choices=PEDIDOS_CHOICE)


