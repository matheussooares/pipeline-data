import csv
# criar uma lista de listas
def table(data,columns_name):
    # reader nome das colunas
    dados_combinados_tabela = [columns_name]
    # itera sobre os dados
    for row in data:
        linha = []
        # Percore os nomes das colunas, caso nao exista coloca indisponível
        for coluna in columns_name:
            linha.append(row.get(coluna, 'Indisponivel'))
        dados_combinados_tabela.append(linha)
    return dados_combinados_tabela

def load_table(data,path):
    with open(path,'w') as file:
        whiter = csv.writer(file)
        whiter.writerows(data)