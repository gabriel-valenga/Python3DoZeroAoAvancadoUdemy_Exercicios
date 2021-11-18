from pessoa import Pessoa
from typing import Union
from conta_poupanca import ContaPoupanca
from conta_corrente import ContaCorrente


class Cliente(Pessoa):
    """
    Classe que representa um cliente.
    Essa classe herda da classe Pessoa

    Métodos:

    __init__(nome: str, idade: int, conta: ContaCorrente, ContaPoupanca)
        Inicializa o cliente
    """
    def __init__(self, nome: str, idade: int, conta: Union[ContaCorrente, ContaPoupanca]):
        """
        Função que inicializa o Cliente.
        :param nome: nome do Cliente
        :type nome: str
        :param idade: idade do CLiente
        :type idade: int
        :param conta: conta (conta corrente ou conta poupança) do Cliente
        :type conta: ContaCorrente, ContaPoupanca
        """
        super().__init__(nome, idade)
        self.conta = conta


