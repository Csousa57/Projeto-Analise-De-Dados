import pandas as pd 

df = pd.read_csv ('ClassicDisco.csv')
#somente as 5 Primeiras linhas 

#print(df.head())
#print(df.shape) # imprime a quantidade de linhas 
# print (df.colums) para aparecer a quantidade de colunas
for i , colunas in enumerate (df.columns):
    print(f" {i}ª colunas, {colunas}")