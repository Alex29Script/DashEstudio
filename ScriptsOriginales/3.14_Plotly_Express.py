import plotly.express as px
import pandas as pd

df_pais = pd.read_excel(r'C:\Users\ivan_pinar\Dropbox\Creación de MOCs\MOC Dash Python\Datasets\3.14\Info_pais.xlsx')

fig1 = px.bar(df_pais, x="País", y="Esperanza de vida", color="Continente")
fig1.show()

fig2 = px.scatter(df_pais, x="Renta per capita", y="Esperanza de vida", color="Continente", size="Poblacion")
fig2.show()
