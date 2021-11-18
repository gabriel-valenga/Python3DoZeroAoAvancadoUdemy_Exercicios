from typing import Union
from cliente import Cliente
from desafio_poo_sistema_bancario.agencia import Agencia
from desafio_poo_sistema_bancario.conta_corrente import ContaCorrente
from desafio_poo_sistema_bancario.conta_poupanca import ContaPoupanca


class Banco:
    """
    Essa classe representa um Banco

    Atributos:

    nome
        nome do Banco
        :type: str
    agencias
        lista de Agencias que pertencem ao Banco
        :type: list()

    clientes
        lista de Clientes que pertencem ao Banco
        :type: list()

    contas
        lista de Contas que pertencem ao Banco
        :type: list()

    Métodos:

    __init__(nome: str)
        Função para inicializar o Banco

    add_agencia(agencia: Agencia):
        Função para adicionar uma agencia na lista de agencias do Banco

    add_cliente(cliente: Cliente):
        Função para adicionar um cliente na lista de clientes do Banco

    add_conta(conta: ContaCorrente, ContaPoupanca):
        Função para adicionar uma conta na lista de contas do Banco


    """
    def __init__(self, nome: str):
        """
        Função que inicializa o Banco
        :param nome: nome do Banco
        :type nome: str
        """
        self._nome = nome
        self._agencias = []
        self._clientes = []
        self._contas = []


    def add_agencia(self, agencia: Agencia):
        """
        Função para cadastrar uma Agencia na lista de Agencias do Banco
        :param agencia: agencia bancária
        :type agencia: Agencia
        """
        self.agencias.append(agencia)

    def add_cliente(self, cliente: Cliente):
        """
        Função para cadastrar um cliente na lista de Clientes do Banco
        :param cliente: cliente do banco
        :type cliente: Cliente
        """
        self.clientes.append(cliente)

    def add_conta(self, conta: Union[ContaCorrente, ContaPoupanca]):
        """
        Função para cadastrar uma Conta na lista de Contas do Banco
        :param conta: conta bancária
        :type conta: ContaCorrente, ContaPoupanca
        """
        self.contas.append(conta)

    def autenticar(self, cliente: Cliente) -> bool:
        """
        Função para autenticar o Cliente no acesso ao Banco
        :param cliente: Cliente que irá acessar o Banco
        :return: bool
        """
        if cliente not in self.clientes:
            return False
        else:
            if cliente.conta not in self.contas:
                return False
            else:
                return True

    @property
    def nome(self):
        """
        nome do Banco
        :return: str
        """
        return self._nome

    @property
    def agencias(self):
        """
        lista de Agencias que pertencem ao Banco
        :return: list()
        """
        return self._agencias

    @property
    def clientes(self):
        """
        lista de Clientes que estão cadastrados no Banco
        :return: list()
        """
        return self._clientes

    @property
    def contas(self):
        """
        lista de Contas que estão cadastradas no Banco
        :return: list()
        """
        return self._contas
