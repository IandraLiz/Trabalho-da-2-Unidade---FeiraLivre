# Generated by Django 4.2.3 on 2024-04-17 23:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='frutas',
            options={'verbose_name_plural': 'Frutas'},
        ),
        migrations.AlterModelOptions(
            name='verduras',
            options={'verbose_name_plural': 'Verduras'},
        ),
        migrations.RenameField(
            model_name='entrega',
            old_name='dtEntrega',
            new_name='dataEntrega',
        ),
        migrations.RenameField(
            model_name='entrega',
            old_name='endrNtrg',
            new_name='enderecoEntrega',
        ),
        migrations.RenameField(
            model_name='entrega',
            old_name='nmClnt',
            new_name='nomeCliente',
        ),
        migrations.RenameField(
            model_name='frutas',
            old_name='prcFrt',
            new_name='custoPorUnidade',
        ),
        migrations.RenameField(
            model_name='frutas',
            old_name='qntdDspnvl',
            new_name='estoqueDeProduto',
        ),
        migrations.RenameField(
            model_name='frutas',
            old_name='nmeFrt',
            new_name='nomeProduto',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='entrega',
            new_name='entregaItem',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='nmItm',
            new_name='nomeItem',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='prcUnit',
            new_name='precoPorUnidade',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='qntdd',
            new_name='quantidadeDeItens',
        ),
        migrations.RenameField(
            model_name='pagamento',
            old_name='mtPgto',
            new_name='metodoPagamento',
        ),
        migrations.RenameField(
            model_name='pagamento',
            old_name='vlrTotal',
            new_name='valorTotal',
        ),
        migrations.RenameField(
            model_name='verduras',
            old_name='pXcVdX',
            new_name='custoPorUnidade',
        ),
        migrations.RenameField(
            model_name='verduras',
            old_name='stkVxL',
            new_name='estoqueDeProduto',
        ),
        migrations.RenameField(
            model_name='verduras',
            old_name='nmVdx',
            new_name='nomeProduto',
        ),
    ]