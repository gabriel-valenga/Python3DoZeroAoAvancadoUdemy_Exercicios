from conta import Conta


class ContaPoupanca(Conta):
    """
    Classe que representa uma conta poupança
    Essa classe herda da classe Conta

    Métodos:

    sacar(valor: float)
        Função para subtrair o valor passado por parâmetro do saldo.
    """
    def sacar(self, valor: float):
        """
        Função para subtrair o valor passado por parâmetro do saldo.
        Se o valor passado por parâmetro for maior que o saldo, não será realizado o saque,
        e irá gerar uma exceção com a mensagem: Saldo insuficiente.
        :param valor: valor a ser sacado
        :type valor: float
        """
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            raise Exception('Saldo insuficiente')
