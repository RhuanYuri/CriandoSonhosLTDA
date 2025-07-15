from datetime import date
import time
import sys
from pathlib import Path

# Caminhos para importação
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

# Importações do sistema
from model.item import Item
from controler.itemControler import ItemControler

class Janela3:

    @staticmethod
    def mostrar_janela3(database_name: str) -> None:
        """
        View para cadastro de itens
        """
        print('----------Cadastro de Item do Menu----------\n')

        while True:
            deseja_continuar = input('Deseja continuar? y-Sim, n-Nao: ').strip().lower()
            if deseja_continuar not in ['y', 'n', 'sim', 'nao']:
                print("Entrada inválida. Digite 'y' ou 'n'.")
                continue
            break

        if deseja_continuar in ['n', 'nao']:
            print('Voltando ao Menu inicial')
            time.sleep(2)
            return

        # Coleta de dados com validação
        nome = input('Nome do item: ').strip()

        while True:
            preco_input = input('Preço do item: ').strip().replace(',', '.')
            try:
                preco = float(preco_input)
                break
            except ValueError:
                print('Preço inválido. Digite um número (use ponto para decimais).')

        tipo = input('Tipo do item: ').strip()
        descricao = input('Descrição do item: ').strip()

        objetoItem = Item(nome, preco, tipo, descricao)

        while True:
            confirma = input('Cadastrar item (y-Sim, n-Nao): ').strip().lower()
            if confirma in ['y', 'sim']:
                ItemControler.insert_into_item(database_name, objetoItem)
                print('Item cadastrado com sucesso!')
                break
            elif confirma in ['n', 'nao']:
                print('Operação cancelada. Voltando ao menu...')
                break
            else:
                print('Opção inválida. Digite "y" ou "n".')

        time.sleep(2)
