#Importación de librerías
import plotly.offline as pyo
import plotly.graph_objs as go
from plotly import subplots
import pandas as pd

#Carga de datos
df_temp = pd.read_csv(r'C:\Users\ivan_pinar\Dropbox\Creación de MOCs\MOC Dash Python\Datasets\3.12\Temperatura_horaria.csv',encoding = 'ISO-8859-1',delimiter=';')

#Definición de objeto de tipo lista "data", en un heatmap intervienen 3 variables x, y, z
data = [go.Heatmap(x=df_temp["Día"], y=df_temp["Hora"], z=df_temp["T_prom"].values.tolist(), colorscale="Jet")] #z debe ser una lista de Python

#Definición de objeto "layout": diseño del gráfico como título, nombres de ejes,...
layout = go.Layout(title = "Heatmap temperatura")

#Creación de objeto "Figure" de Plotly a partir de los objetos data y layout creados previamente
fig = go.Figure(data=data, layout=layout)
#Generación del plot a partir de la figura definida y nombre del fichero de salida HTML
pyo.plot(fig, filename="3.12 Heatmap Temp.html")

#Crear subplots
trace1 = go.Heatmap(x=df_temp["Día"], y=df_temp["Hora"], z=df_temp["T_prom"].values.tolist()) #z debe ser una lista de Python
trace2 = go.Heatmap(x=df_temp["Día"], y=df_temp["Hora"], z=df_temp["T_prom"].values.tolist(), colorscale="Jet") #z debe ser una lista de Python

#Creación subplots con 1 fila y 2 columnas
fig2 = subplots.make_subplots(rows = 1, cols = 2, subplot_titles=["Normal", "Jet"], shared_yaxes=False)
#Añadimos las trazas a la figura (fig2)
fig2.append_trace(trace1,1,1)
fig2.append_trace(trace2,1,2)
#Generación del plot a partir de la figura definida y nombre del fichero de salida HTML
pyo.plot(fig2, filename="3.12 Heatmap Temp_mult.html")
