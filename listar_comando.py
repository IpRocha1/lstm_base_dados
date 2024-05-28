import pandas as pd
import re

# Carregar o arquivo CSV
df = pd.read_csv('data_frame_python_tratado.csv')

# Remover linhas onde 'sourceCode' é NaN
df = df.dropna(subset=['sourceCode'])

# Função para extrair comandos print
def extract_prints(code):
    print_commands = []
    lines = code.split('\n')
    for line in lines:
        stripped_line = line.strip()
        if stripped_line.startswith('print(') or re.match(r'print\s*\(.*\)', stripped_line):
            print_commands.append(stripped_line)
    return print_commands

# Listar todos os comandos print
all_prints = []
for code in df['sourceCode']:
    all_prints.extend(extract_prints(code))

# Salvar os comandos print em um arquivo .txt
with open('comandos_print3.txt', 'w', encoding='utf-8') as f:
    for print_command in all_prints:
        f.write(print_command + '\n')

