produtos = ['Produto A','Produto B','Produto C']
estoque_inicial = [100, 150, 200]
vendas_mensais = [30, 50, 70]

estoque_restante = [estoque - vendas for estoque, vendas in zip(estoque_inicial, vendas_mensais)]

relatorio = [
    {
        'Produto': produto,
        'Estoque Inicial': estoque,
        'Vendas Mensais': vendas,
        'Estoque Restante': restante
    }
    for produto, estoque, vendas, restante in zip(produtos, estoque_inicial, vendas_mensais, estoque_restante)
]

print(relatorio)