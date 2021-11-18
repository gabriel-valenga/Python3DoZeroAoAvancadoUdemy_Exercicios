from abc import ABC, abstractmethod


class Conta(ABC):
    """
    Classe abstrata que representa uma conta

    Métodos:

    __init__(agencia: int, numero_conta: int, saldo: float)
        Inicializa a conta

    depositar(valor: float)
        Adiciona o valor passado por parâmetro ao saldo

    sacar(valor: float)
        Método abstrato

    """
    def __init__(self, agencia: int, numero_conta: int, saldo: float):
        """
        Função que inicializa a Conta
        :param agencia: número da agência
        :type agencia: int
        :param numero_conta: número da conta
        :type numero_conta: int
        :param saldo: saldo da conta
        :type saldo: int
        """
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.saldo = 0
        self.depositar(saldo)

    def depositar(self, valor: float):
        """
        Função para acrescentar o valor passado por parâmetro ao saldo.
        :param valor: valor a ser acrescentado ao saldo
        :type valor: float
        """
        self.saldo += valor

    @abstractmethod
    def sacar(self, valor: float):
        """
        Método abstrato que deve ser implementado nas classes filhas
        :type valor: float
        """
        pass
