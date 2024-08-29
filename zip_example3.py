# Listas de dados sobre tarefas, prioridades e responsáveis
tarefas = ['Tarefa 1', 'Tarefa 2', 'Tarefa 3', 'Tarefa 4']
prioridades = ['Alta', 'Média', 'Alta', 'Baixa']
responsaveis = ['Ana', 'Bob', 'Ana', 'Bob']

# Calculando o número de tarefas por responsável
from collections import Counter

contagem_tarefas = Counter(responsaveis)

# Criando uma lista de dicionários com informações detalhadas
relatorio_tarefas = [
    {
        'Tarefa': tarefa,
        'Prioridade': prioridade,
        'Responsável': responsavel
    }
    for tarefa, prioridade, responsavel in zip(tarefas, prioridades, responsaveis)
]

# Criando o relatório final que inclui a contagem de tarefas por responsável
relatorio_final = {
    'Tarefas': relatorio_tarefas,
    'Contagem por Responsável': dict(contagem_tarefas)
}

print(relatorio_final)
