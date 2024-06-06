#Importación de librerías
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

#Carga de datos
df_temp = pd.read_excel(r'C:\Users\ivan_pinar\Dropbox\Creación de MOCs\MOC Dash Python\Datasets\3.8\Temperaturas.xlsx')

#Definición de objeto de tipo lista "data", x --> Categorízación, y --> Valores a verificar distribución
data = [go.Box(x=df_temp["Ciudad"],y=df_temp["T_Promedio"])] #pointpos=0 para ubicación de los puntos en el centro / boxpoints ="all" si se quieren visualizar todos los puntos

#Definición de objeto "layout": diseño del gráfico como título, nombres de ejes,...
layout = go.Layout(title="Box & whiskers Temperatura")

#Creación de objeto "Figure" de Plotly a partir de los objetos data y layout creados previamente
fig = go.Figure(data=data, layout=layout)
#Generación del plot a partir de la figura definida y nombre del fichero de salida HTML
pyo.plot(fig, filename="3.8 Temp_Box Plot.html")
