from banco import Banco
from agencia import Agencia
from cliente import Cliente
from conta_corrente import ContaCorrente
from conta_poupanca import ContaPoupanca


def ir_ao_banco(banco: Banco, agencia: Agencia, cliente: Cliente):
    if agencia in banco.agencias:
        if cliente in banco.clientes:
            if banco.autenticar(cliente):
                while True:
                    try:
                        operacao = input('1 - sacar / 2 - depositar / 3 - ver saldo/ 0 - sair')
                        if operacao == '1':
                            valor = float(input('Digite o valor do saque:'))
                            cliente.conta.sacar(valor)
                        elif operacao == '2':
                            valor = float(input('Digite o valor do depósito:'))
                            cliente.conta.depositar(valor)
                        elif operacao == '3':
                            print(cliente.conta.saldo)
                        elif operacao == '0':
                            break
                        else:
                            print('Operação inválida! Digite novamente')
                    except Exception as e:
                        print(e)
            else:
                print(f'Cliente não autenticado.')

        else:
            print(f'Cliente não tem cadastro no banco {banco.nome}.')
    else:
        print(f'Agência errada.')


banco_1 = Banco('Banco 1')
banco_2 = Banco('Banco 2')
agencia_a = Agencia(1, 'Rua das Couves, 71')
agencia_b = Agencia(2, 'Rua das Couves, 21')
banco_1.add_agencia(agencia_a)
banco_2.add_agencia(agencia_b)
conta_1 = ContaCorrente(agencia_a.agencia_id, 1, 500, 1000)
conta_2 = ContaPoupanca(agencia_a.agencia_id, 2, 1000)
conta_3 = ContaPoupanca(agencia_a.agencia_id, 3, 9000)
banco_1.add_conta(conta_1)
banco_1.add_conta(conta_2)
banco_1.add_conta(conta_3)
jose = Cliente('José', 45, conta_1)
gabriel = Cliente('Gabriel', 23, conta_2)
carlos = Cliente('Carlos', 48, conta_3)
banco_1.add_cliente(gabriel)
banco_1.add_cliente(jose)
banco_1.add_cliente(carlos)

ir_ao_banco(banco_1, agencia_a, jose)

