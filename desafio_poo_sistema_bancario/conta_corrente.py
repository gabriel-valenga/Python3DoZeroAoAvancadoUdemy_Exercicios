from conta import Conta


class ContaCorrente(Conta):
    """
    Classe que representa uma conta corrente
    Essa classe herda da classe Conta

    Métodos:

    __init__(agencia: int, numero_conta: int, saldo: float, limite_saque: float)
        Inicializa a ContaCorrente

    sacar(valor: float) -> bool
        Função para subtrair o valor passado por parâmetro do saldo.

    """
    def __init__(self, agencia: int, numero_conta: int, saldo: float, limite_saque: float):
        """
        Função que inicializa a ContaCorrente
        :param agencia: número da agência
        :type agencia: int
        :param numero_conta: número da conta corrente
        :type numero_conta: int
        :param saldo: saldo da conta corrente
        :type saldo: float
        :param limite_saque: valor máximo para fazer saque na conta corrente
        :type limite_saque: float
        """
        super().__init__(agencia, numero_conta, saldo)
        self.limite_saque = limite_saque

    def sacar(self, valor: float) -> bool:
        """
        Função para substrair do saldo o valor passado por parâmetro.
        Se o valor passado por parâmetro for maior que o saldo, não será realizado o saque,
        e irá gerar uma exceção com a mensagem: Saldo insuficiente.
        Se o valor passado por parâmetro for maior que o limite_saque, não será realizado o saque,
        e irá gerar uma exceção com a mensagem: Saque não permitido, valor acima do limite.
        :param valor: valor a ser sacado
        :type valor: float
        :return: bool
        """
        if valor > self.limite_saque:
            raise Exception('Saque não permitido, valor acima do limite')
        if valor > self.saldo:
            raise Exception('Saldo insuficiente.')
        return True

