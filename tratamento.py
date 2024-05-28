import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv('data_frame_python2.csv')

# Remover linhas com codigos vazios
df = df.dropna(subset=['sourceCode'])

# Funcao para remover linhas de comentarios
def remove_comments(code):
    lines = code.split('\n')
    non_comment_lines = []
    for line in lines:
        if not line.strip().startswith('#'):
            non_comment_lines.append(line)
    return '\n'.join(non_comment_lines)

# Aplicar a funcao na coluna 'sourceCode'
df['sourceCode'] = df['sourceCode'].apply(remove_comments)

# Salvar o novo DataFrame em um novo arquivo CSV
df.to_csv('data_frame_python_tratado.csv', index=False)
print(df)