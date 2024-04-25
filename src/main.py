from pipelinedata.extract import read
from pipelinedata import transform
from pipelinedata import load

path_json = r'C:\Users\je7560\Downloads\matheus\pipeline-data\src\data\raw\dados_empresaA.json'
path_csv = r'C:\Users\je7560\Downloads\matheus\pipeline-data\src\data\raw\dados_empresaB.csv'

# Carregar os dados
data_A = read(path_json,'json').data
data_B = read(path_csv,'csv').data

# Transformando os dados
name_columns = transform.get_columns(data_B)

key_mapping = {'Nome do Item': 'Nome do Produto',
                'ClassificaÃ§Ã£o do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}

datatransf_csv = transform.rename_columns(data_B, key_mapping)

data = transform.data_join(data_A,datatransf_csv)

print(f"Tamanho do dados combinados: {len(data)}")

# Carregar os dados
path_data = r'C:\Users\je7560\Downloads\matheus\pipeline-data\src\data\ready-processed\data.csv'
data_table =  load.table(data,name_columns)

load.load_table(data_table,path_data)