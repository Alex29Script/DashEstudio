#Importación de librerías
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

#Carga de datos
df_temp = pd.read_excel(r'C:\Users\ivan_pinar\Dropbox\Creación de MOCs\MOC Dash Python\Datasets\3.9\Temperaturas.xlsx')

#Definición de objeto de tipo lista "data"
data = [go.Histogram(x=df_temp["T_Promedio"],xbins=dict(start=0,end=40,size=5),histnorm='probability',cumulative_enabled=True)] #cumulative_enabled=True para CDF / nbinsx para especificar número de bins directamente

#Definición de objeto "layout": diseño del gráfico como título, nombres de ejes,...
layout = go.Layout(title="Histograma Temperatura")

#Creación de objeto "Figure" de Plotly a partir de los objetos data y layout creados previamente
fig = go.Figure(data=data, layout=layout)
#Generación del plot a partir de la figura definida y nombre del fichero de salida HTML
pyo.plot(fig, filename="3.9 Histograma.html")
