estudantes = ['Gustavo','Ulquiorra', 'Aizen', 'Yhwach', 'Misa']
matematica = [7.0,7.0,7.0,7.0,7.0]
portugues = [8.0,8.0,8.0,8.0,8.0]
historia = [9.0,9.0,9.0,9.0,9.0]

resultado = [
    {
        'Nome': estudante,
        'Matematica': nota_matematica,
        'Portugues': nota_portugues,
        'Historia': nota_historia
    }
    for estudante, nota_matematica,nota_portugues,nota_historia in zip(estudantes, matematica,portugues,historia)
]
print(resultado)
