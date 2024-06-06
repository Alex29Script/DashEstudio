#Importación de librerías
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

#Carga de datos
df_ventas = pd.read_csv(r'...ruta_local...',encoding = 'ISO-8859-1',delimiter=';')

#Definición de objeto de tipo lista "data": datos utilizados en el gráfico y el tipo de gráfico. Uso de diferentes trazas
trace0 = go.Scatter(...)

trace1 = go.Scatter(...)

data = [trace0, trace1]

#Definición de objeto "layout": diseño del gráfico como título, nombres de ejes,...
layout = go.Layout(...)

#Creación de objeto "Figure" de Plotly a partir de los objetos data y layout creados previamente
fig = go.Figure(...)
#Generación del plot a partir de la figura definida y nombre del fichero de salida HTML
pyo.plot(...)
