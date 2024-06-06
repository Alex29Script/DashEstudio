#Importación de librerías
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

#Carga de datos
df_med = pd.read_excel(r'C:\Users\ivan_pinar\Dropbox\Creación de MOCs\MOC Dash Python\Datasets\3.5\Medallas_olímpicas.xlsx')

#Ordenar descendentemente por la columna "Total"
df_med = df_med.sort_values(by="Total",ascending=False)

#Definición de objeto de tipo lista "data" con 1 única traza basada en el Total de medallas
#data = [go.Bar(x=df_med["País"], y=df_med["Total"])]

#Definición de objeto de tipo lista "data" con 3 trazas, 1 para cada tipo de medalla
trace0 = go.Bar(x=df_med["País"], y=df_med["Oro"], name="Oro", marker={"color":"#FFD700"}) #Definimos el color de la barra con el argumento marker
trace1 = go.Bar(x=df_med["País"], y=df_med["Plata"], name="Plata", marker={"color":"#C0C0C0"})
trace2 = go.Bar(x=df_med["País"], y=df_med["Bronce"], name="Bronce", marker={"color":"#CD7F32"})
data = [trace0,trace1,trace2]

#Definición de objeto "layout": diseño del gráfico como título, nombres de ejes,...
layout = go.Layout(title="Medallas olímpicas por país",
                    xaxis=dict(title="País"),
                    yaxis=dict(title="Total medallas"),
                    barmode="stack"
                    ) #Se define el barmode = "stack" para columnas apiladas

#Creación de objeto "Figure" de Plotly a partir de los objetos data y layout creados previamente
fig = go.Figure(data=data, layout=layout)
#Generación del plot a partir de la figura definida y nombre del fichero de salida HTML
pyo.plot(fig, filename="3.5_Bar plot medallas.html")
