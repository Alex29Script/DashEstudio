#Importación de librerías
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

#Carga de datos
df_iris = pd.read_csv(r'C:\Users\ivan_pinar\Dropbox\Creación de MOCs\MOC Dash Python\Datasets\3.2\iris_dataset.csv',encoding = 'ISO-8859-1',delimiter=',')

#Definición de objeto de tipo lista "data": datos utilizados en el gráfico y el tipo de gráfico
data = [go.Scatter(x=df_iris["longitud_sépalo"],
                    y=df_iris["anchura_sépalo"],
                    mode="markers",
                    marker = dict(
                            size=12,
                            symbol="circle",
                            line={"width":3} #línea del marcador
                    ))]

#Definición de objeto "layout": diseño del gráfico como título, nombres de ejes,...
layout = go.Layout(title="Iris Scatter plot",
                    xaxis=dict(title="Longitud sépalo"),
                    yaxis=dict(title="Anchura sépalo"))

#Creación de objeto "Figure" de Plotly a partir de los objetos data y layout creados previamente
fig = go.Figure(data=data, layout=layout)

#Generación del plot a partir de la figura definida y nombre del fichero de salida HTML
pyo.plot(fig, filename="3.2_Plot Scatter Iris.html")
