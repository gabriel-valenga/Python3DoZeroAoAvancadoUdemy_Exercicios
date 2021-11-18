class Agencia:
    """
    Classe que representa uma agência bancária

    Atributos:

    agencia_id
        número da agência
        :type: int

    Métodos:

    __init__(agencia_id: int, endereco: str):
        Função para inicializar a Agencia
    """
    def __init__(self, agencia_id: int, endereco: str):
        """
        Função que inicializa a Agencia
        :param agencia_id: número da Agencia
        :type agencia_id: int
        :param endereco: endereço da Agencia
        :type endereco: str
        """
        self._agencia_id = agencia_id
        self._endereco = endereco

    @property
    def agencia_id(self):
        """
        Número da Agencia
        :return: int
        """
        return self._agencia_id
