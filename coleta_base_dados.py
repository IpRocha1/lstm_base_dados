import requests
import pandas as pd
import time
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

url = 'https://onlinejudge.u-aizu.ac.jp/solutions/search'

# Simulador de browser
service = Service(ChromeDriverManager().install())

chrome = webdriver.ChromeOptions()
chrome.add_argument('--headless')
chrome.add_argument('--no-sandbox')
chrome.add_argument('--disable-dev-shm-usage')

browser = webdriver.Chrome(service=service, options=chrome)
browser.get(url)

site = BeautifulSoup(browser.page_source, "html.parser")

lista_nomes = site.find_all('div', {'class':'info'})
print(lista_nomes)

browser.quit()

df = pd.DataFrame(columns=['judgeId','problemId','sourceCode'])

judgeId = []
# for i in range(1,9996):
#     print('Problema', i)
#     j = str(i).zfill(4)
    
#     response = requests.get(f"https://judgeapi.u-aizu.ac.jp/solutions/problems/{j}/lang/python3")
#     dados = response.json()
#     for dado in dados:
#         politica = dado["policy"]
#         if politica == "public":
#             judgeId.append(dado["judgeId"])
    
#     # response = requests.get(f"https://judgeapi.u-aizu.ac.jp/solutions/problems/ALDS1_{i}_A/lang/python3")
#     # dados = response.json()
#     # for dado in dados:
#     #     politica = dado["policy"]
#     #     if politica == "public":
#     #         judgeId.append(dado["judgeId"])

#     # response = requests.get(f"https://judgeapi.u-aizu.ac.jp/solutions/problems/ALDS1_{i}_B/lang/python3")
#     # dados = response.json()
#     # for dado in dados:
#     #     politica = dado["policy"]
#     #     if politica == "public":
#     #         judgeId.append(dado["judgeId"])

#     # response = requests.get(f"https://judgeapi.u-aizu.ac.jp/solutions/problems/ALDS1_{i}_C/lang/python3")
#     # dados = response.json()
#     # for dado in dados:
#     #     politica = dado["policy"]
#     #     if politica == "public":
#     #         judgeId.append(dado["judgeId"])

#     # response = requests.get(f"https://judgeapi.u-aizu.ac.jp/solutions/problems/ALDS1_{i}_D/lang/python3")
#     # dados = response.json()
#     # for dado in dados:
#     #     politica = dado["policy"]
#     #     if politica == "public":
#     #         judgeId.append(dado["judgeId"])

# print(len(judgeId))
# for id in judgeId:
    
#     try:
#         response = requests.get(f"https://judgeapi.u-aizu.ac.jp/reviews/{id}")
#         dado = response.json()
#         id_judge = dado["judgeId"]
#         id_problem = dado["problemId"]
#         codigo = dado["sourceCode"]
#         time.sleep(5)
#     except requests.exceptions.ConnectionError:
#         time.sleep(5)
#         # print(id)
        
#     df_novo = pd.DataFrame([[id_judge,id_problem,codigo]], columns=df.columns)
#     df = pd.concat([df,df_novo], ignore_index=True)
#     print(df)
# df.to_csv('data_frame_python.csv', index=False)
# print(df)