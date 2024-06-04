import pandas as pd

problemName = 'Gossip'

# Carregar o arquivo CSV
data = pd.read_csv('./dataframe/data_frame_python_tratado.csv')

# Filtrar as linhas pelo nome do problemName
problemName_df = data[data['problemName'] == problemName]

# Salvar o resultado em um novo arquivo CSV
problemName_df.to_csv(f'./data_fragment/ProblemName_{problemName}_data.csv', index=False)

# Verificar as primeiras linhas do DataFrame filtrado
print(problemName_df.head())
