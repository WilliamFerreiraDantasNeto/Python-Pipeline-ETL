import pandas as pd

df = pd.read_csv('Character.csv')
Charid = df['CharID'].tolist()

tabela = pd.read_excel('Background.xlsx')

print(list(tabela['Kit']))