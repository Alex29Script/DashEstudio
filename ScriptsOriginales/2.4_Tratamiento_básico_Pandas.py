import pandas as pd

df = pd.read_csv(r'C:\Users\ivan_pinar\Dropbox\Creación de MOCs\MOC Dash Python\Datasets\2.3\Info_pais.csv',encoding = 'ISO-8859-1',delimiter=';')


df_filtrado = df[df["Poblacion"]>150000000]

print(df_filtrado[["País","Poblacion"]])
