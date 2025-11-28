import pandas as pd 

df = pd.read_csv ('ClassicDisco.csv')
# filtra musicas lançadas após 1980

#print(df[df["Year"]>1980])
print(df[df["Year"]>1980][['Year','Track']])