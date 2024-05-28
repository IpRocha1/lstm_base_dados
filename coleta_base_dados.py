import requests
import pandas as pd
import time

# url = 'https://onlinejudge.u-aizu.ac.jp/solutions/search'


df = pd.DataFrame(columns=['judgeId','problemId', 'problemName', 'sourceCode'])

problemas_nomes = {}
for k in range(0,4):
    response1 = requests.get(f'https://judgeapi.u-aizu.ac.jp/problems?page={k}&size=1000')
    problemas = response1.json()
    for problema in problemas:
        id_problema = problema["id"]
        nome_problema = problema["name"]
        problemas_nomes[id_problema] = nome_problema

print('Qtd de problemas', len(problemas_nomes))
judgeId = []
for chave in problemas_nomes.keys():
    
    try:
        response = requests.get(f"https://judgeapi.u-aizu.ac.jp/solutions/problems/{chave}/lang/python3")
        time.sleep(1)

        dados = response.json()
        for dado in dados:
            politica = dado["policy"]
            if politica == "public":
                judgeId.append(dado["judgeId"])
    except requests.exceptions.ConnectionError:
        time.sleep(1)

print('Quantidade de julgamentos', len(judgeId))
for id in judgeId:
    
    try:
        response = requests.get(f"https://judgeapi.u-aizu.ac.jp/reviews/{id}")
        dado = response.json()
        id_judge = dado["judgeId"]
        id_problem = dado["problemId"]
        name_problem = problemas_nomes[id_problem]
        codigo = dado["sourceCode"]
        time.sleep(1)
    except requests.exceptions.ConnectionError:
        time.sleep(1)
        # print(id)
        
    df_novo = pd.DataFrame([[id_judge,id_problem,name_problem, codigo]], columns=df.columns)
    df = pd.concat([df,df_novo], ignore_index=True)
    print(len(df))
df.to_csv('data_frame_python2.csv', index=False)
print(df)