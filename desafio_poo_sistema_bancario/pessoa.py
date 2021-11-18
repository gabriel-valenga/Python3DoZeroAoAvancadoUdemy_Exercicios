class Pessoa:
    """
    Classe que representa uma pessoa

    Atributos:

    nome: str
        Nome da pessoa
    idade: int
        Idade da pessoa

    Métodos:

    __init__(nome: str, idade: int)
        Inicializa a pessoa
    """
    def __init__(self, nome: str, idade: int):
        """
        Função que inicializa a Pessoa.
        :param nome: nome da Pessoa
        :type nome: str
        :param idade: idade da Pessoa
        :type idade: int
        """
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        """
        nome da Pessoa
        :return: str
        """
        return self._nome

    @property
    def idade(self):
        """
        idade da Pessoa
        :return: int
        """
        return self._idade
    