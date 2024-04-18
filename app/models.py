from django.db import models

class Produto(models.Model):
    nomeProduto = models.CharField(max_length=100)
    custoPorUnidade = models.DecimalField(max_digits=6, decimal_places=2)
    estoqueDeProduto = models.IntegerField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.nomeProduto
    
class Verduras(Produto):
    class Meta:
        verbose_name_plural = "Verduras"

class Frutas(Produto):
    class Meta:
        verbose_name_plural = "Frutas"

class Entrega(models.Model):
    nomeCliente = models.CharField(max_length=255)
    enderecoEntrega = models.TextField()
    dataEntrega = models.DateTimeField()
    pagamento = models.OneToOneField('Pagamento', on_delete=models.CASCADE, related_name='entrega')

    def __str__(self):
        return f"Entrega de {self.nomeCliente} em {self.enderecoEntrega}"

class Pagamento(models.Model):
    metodoPagamento = models.CharField(max_length=50)
    valorTotal = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.metodoPagamento

class Item(models.Model):
    entregaItem = models.ForeignKey(Entrega, on_delete=models.CASCADE, related_name="itens")
    nomeItem = models.CharField(max_length=100)
    quantidadeDeItens = models.IntegerField()
    precoPorUnidade = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"Item de {self.nomeItem}"
    