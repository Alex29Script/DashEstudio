#Importación de librerías
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

#Carga de datos
df_sp500 = pd.read_csv(r'C:\Users\ivan_pinar\Dropbox\Creación de MOCs\MOC Dash Python\Datasets\3.3\SP500_data_.csv',encoding = 'ISO-8859-1',delimiter=',')

#Definición de objeto de tipo lista "data": datos utilizados en el gráfico y el tipo de gráfico. Uso de diferentes trazas
trace0 = go.Scatter(x=df_sp500["Date"],
                    y=df_sp500["Close"],
                    mode="lines", #lines+markers para representar en la misma traza la línea y los markers
                    name="Cierre")

trace1 = go.Scatter(x=df_sp500["Date"],
                    y=df_sp500["Open"],
                    mode="lines", #lines+markers para representar en la misma traza la línea y los markers
                    name="Apertura")

data = [trace0, trace1]

#Definición de objeto "layout": diseño del gráfico como título, nombres de ejes,...
layout = go.Layout(title="SP500 Line plot",
                    xaxis=dict(title="Fecha"),
                    yaxis=dict(title="SP500 valor"))

#Creación de objeto "Figure" de Plotly a partir de los objetos data y layout creados previamente
fig = go.Figure(data=data, layout=layout)
#Generación del plot a partir de la figura definida y nombre del fichero de salida HTML
pyo.plot(fig, filename="3.3_Line plot SP500.html")
