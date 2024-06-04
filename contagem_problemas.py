import pandas as pd

# Carregar o arquivo CSV
data = pd.read_csv('data_frame_python_tratado.csv')

# Contagem de problemName
contagem_problemName = data['problemName'].value_counts()

# Criar DataFrames para as contagens
quantidade_problemas_df = contagem_problemName.reset_index()
quantidade_problemas_df.columns = ['problemName', 'Count']
# Salvar em arquivos CSV
quantidade_problemas_df.to_csv('quantidade_problemas.csv', index=False)