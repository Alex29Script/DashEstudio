#Importación de librerías
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

#Definición de datos (lista de valores)
datos = [11,13,2,5,18,20,18,15,13,25,15,22,7,11]

#Definición de objeto de tipo lista "data", si no hay categorías, solo utilizar el argumento "y" para el gráfico de tipo Box
data = [go.Box(y=datos)] #pointpos=0 para ubicación de los puntos en el centro / boxpoints ="all" si se quieren visualizar todos los puntos

#Definición de objeto "layout": diseño del gráfico como título, nombres de ejes,...
layout = go.Layout(title="Box Plot")

#Creación de objeto "Figure" de Plotly a partir de los objetos data y layout creados previamente
fig = go.Figure(data=data, layout=layout)
#Generación del plot a partir de la figura definida y nombre del fichero de salida HTML
pyo.plot(fig, filename="3.7_Box Plot.html")
