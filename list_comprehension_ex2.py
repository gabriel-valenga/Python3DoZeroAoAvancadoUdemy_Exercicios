carrinho = []

carrinho.append(('Produto 1', 30))
carrinho.append(('Produto 2', 50))
carrinho.append(('Produto 3', 70))

total = sum([valor for produto, valor in carrinho])
print(total)
