#Importación de librerías
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
import numpy as np

#Carga de datos
df_pais = pd.read_excel(r'C:\Users\ivan_pinar\Dropbox\Creación de MOCs\MOC Dash Python\Datasets\3.6\Info_pais.xlsx')

#Definimos un diccionario para asociar cada continente (claves) a un color (valores)
dic_color = {"North America":"green","Asia":"yellow","Europe":"red","South America":"blue","Oceania":"brown","Africa":"orange"}
#Creamos una nueva columna "color_cont" mapeando la columna "Continente" del dataframe a partir del diccionario
df_pais["color_cont"] = df_pais["Continente"].map(dic_color)

print(df_pais.head())

#Definición de objeto de tipo lista "data": datos utilizados en el gráfico y el tipo de gráfico
data = [go.Scatter(x=df_pais["Renta per capita"],
                    y=df_pais["Esperanza de vida"],
                    mode="markers",
                    text=df_pais["País"],
                    marker = dict(
                            size=(df_pais["Poblacion"])/5000000, #Utilizamos el tamaño del marcador en fucnión de la 3º variable "Población", si valores muy elevados, aplicamos un factor corrector
                            color=df_pais["color_cont"] #Utilizamos el color del marcador en función de la 4ª variable "color_cont"
                    ))]

#Definición de objeto "layout": diseño del gráfico como título, nombres de ejes,...
layout = go.Layout(title="Renta per capita vs Esperanza de vida",
                    xaxis=dict(title="Renta per capita"),
                    yaxis=dict(title="Esperanza de vida"))

#Creación de objeto "Figure" de Plotly a partir de los objetos data y layout creados previamente
fig = go.Figure(data=data, layout=layout)
#Generación del plot a partir de la figura definida y nombre del fichero de salida HTML
pyo.plot(fig, filename="3.6_Bubble Plot.html")
