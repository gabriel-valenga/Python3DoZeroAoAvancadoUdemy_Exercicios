import re
from random import randint

LINHA_UM = '543298765432'
LINHA_DOIS = '6543298765432'


def validar(cnpj):
    cnpj = remover_caracteres(cnpj)
    cnpj_original = cnpj
    if len(cnpj) != 14:
        return False
    cnpj_sem_digitos = remover_digitos(cnpj)
    primeiro_digito_gerado = retorna_digito(cnpj_sem_digitos, 1)
    if primeiro_digito_gerado != cnpj_original[12]:
        return False
    cnpj_com_primeiro_digito = cnpj_sem_digitos + primeiro_digito_gerado
    segundo_digito_gerado = retorna_digito(cnpj_com_primeiro_digito, 2)
    if segundo_digito_gerado != cnpj_original[13]:
        return False
    return True


def remover_caracteres(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)


def remover_digitos(cnpj):
    return cnpj[0:12]


def retorna_digito(cnpj_primeira_parte, digito):
    soma = 0
    if digito == 1:
        for i in range(12):
            soma += int(cnpj_primeira_parte[i]) * int(LINHA_UM[i])
    else:
        for i in range(13):
            soma += int(cnpj_primeira_parte[i]) * int(LINHA_DOIS[i])
    resultado = 11 - (soma % 11)
    if resultado > 9:
        resultado = 0
    return str(resultado)


def gerar(formatado=False):
    primeira_parte = ''
    for i in range(8):
        primeira_parte += str(randint(0, 9))
    cnpj = primeira_parte + '0001'
    cnpj += retorna_digito(cnpj, 1)
    cnpj += retorna_digito(cnpj, 2)
    if formatado:
        cnpj = formatar(cnpj)
    return cnpj


def formatar(cnpj):
    return f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}'
