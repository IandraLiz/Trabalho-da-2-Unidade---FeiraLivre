from rest_framework import serializers
from app.models import Verduras, Frutas, Entrega, Pagamento, Item

class VerdurasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Verduras
        fields = ['nomeProduto', 'custoPorUnidade', 'estoqueDeProduto']

class FrutasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Frutas
        fields = ['nomeProduto', 'custoPorUnidade', 'estoqueDeProduto']

class EntregaSerializer(serializers.ModelSerializer):
    itens = serializers.PrimaryKeyRelatedField(many=True, queryset=Item.objects.all())
    pagamento = serializers.PrimaryKeyRelatedField(queryset=Pagamento.objects.all())

    class Meta:
        model = Entrega
        fields = ['nomeCliente', 'enderecoEntrega', 'dataEntrega', 'itens', 'pagamento']

class PagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagamento
        fields = ['metodoPagamento', 'valorTotal']

class ItemSerializer(serializers.ModelSerializer):
    entregaItem = serializers.PrimaryKeyRelatedField(queryset=Entrega.objects.all())

    class Meta:
        model = Item
        fields = ['entregaItem', 'nomeItem', 'quantidadeDeItens', 'precoPorUnidade']
