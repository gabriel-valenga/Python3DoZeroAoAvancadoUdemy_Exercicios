lista = []
lista_refazer = []


def adicionar_tarefa(tarefa_):
    lista.append(tarefa_)


def listar_tarefas():
    for elemento in lista:
        print(elemento)


def desfazer():
    elemento_desfeito = lista.pop()
    lista_refazer.append(elemento_desfeito)


def refazer():
    if len(lista_refazer) > 0:
        ultimo = len(lista_refazer) - 1
        lista.append(lista_refazer[ultimo])
        lista_refazer.pop(ultimo)


while True:
    opcao = int(input(' 1 - Nova tarefa \n 2 - Listar tarefas \n 3 - Desfazer \n 4 - Refazer'))
    if opcao == 1:
        tarefa = input('Digite a tarefa:')
        adicionar_tarefa(tarefa)
    elif opcao == 2:
        listar_tarefas()
    elif opcao == 3:
        desfazer()
    elif opcao == 4:
        refazer()
    else:
        break




