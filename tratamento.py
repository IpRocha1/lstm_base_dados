import pandas as pd
import re

# Carregar o arquivo CSV
df = pd.read_csv('data_frame_python2.csv')

# Remover linhas com codigos vazios
df = df.dropna(subset=['sourceCode'])

# Funcao para remover comentarios (linhas completas e inline)
def remove_comments(code):
    # Remove comentarios de linha unica e inline
    code = re.sub(r'#.*', '', code)
    
    # Remover blocos de comentarios delimitados por ''' ou """
    pattern = re.compile(r'(""".*?"""|\'\'\'.*?\'\'\')', re.DOTALL)
    code = re.sub(pattern, '', code)
    
    # Remover linhas em branco geradas
    lines = code.split('\n')
    non_empty_lines = [line for line in lines if line.strip() != '']
    
    return '\n'.join(non_empty_lines)

# Aplicar a funcao em cada linha de sourceCode
df['sourceCode'] = df['sourceCode'].apply(remove_comments)

# Salvar o novo DataFrame em um novo arquivo CSV
df.to_csv('data_frame_python_tratado.csv', index=False)
print(df)