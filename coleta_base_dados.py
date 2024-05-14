import requests
import pandas as pd
import time

# https://onlinejudge.u-aizu.ac.jp/solutions/search

df = pd.DataFrame(columns=['judgeId','problemId','sourceCode'])


for i in range(3,16):
    judgeId = []
    response = requests.get(f"https://judgeapi.u-aizu.ac.jp/solutions/problems/ALDS1_{i}_A/lang/python3")
    dados = response.json()
    for dado in dados:
        politica = dado["policy"]
        if politica == "public":
            judgeId.append(dado["judgeId"])

    response = requests.get(f"https://judgeapi.u-aizu.ac.jp/solutions/problems/ALDS1_{i}_B/lang/python3")
    dados = response.json()
    for dado in dados:
        politica = dado["policy"]
        if politica == "public":
            judgeId.append(dado["judgeId"])

    response = requests.get(f"https://judgeapi.u-aizu.ac.jp/solutions/problems/ALDS1_{i}_C/lang/python3")
    dados = response.json()
    for dado in dados:
        politica = dado["policy"]
        if politica == "public":
            judgeId.append(dado["judgeId"])

    response = requests.get(f"https://judgeapi.u-aizu.ac.jp/solutions/problems/ALDS1_{i}_D/lang/python3")
    dados = response.json()
    for dado in dados:
        politica = dado["policy"]
        if politica == "public":
            judgeId.append(dado["judgeId"])

    for id in judgeId:
        try:
            response = requests.get(f"https://judgeapi.u-aizu.ac.jp/reviews/{id}")
            dado = response.json()
            id_judge = dado["judgeId"]
            id_problem = dado["problemId"]
            codigo = dado["sourceCode"]
        except requests.exceptions.ConnectionError:
            time.sleep(15)
            continue
        # print(id)
        

        df_novo = pd.DataFrame([[id_judge,id_problem,codigo]], columns=df.columns)
        df = pd.concat([df,df_novo], ignore_index=True)
    df.to_csv(f'{i}_data_frame_python.csv', index=False)
    print(df)