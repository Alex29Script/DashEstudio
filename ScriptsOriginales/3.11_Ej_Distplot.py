#Importación de librerías
import plotly.offline as pyo
import plotly.figure_factory as ff #Nueva librería para gráficos complejos
import pandas as pd

#Carga de datos
df_peatones = pd.read_csv(r'C:\Users\ivan_pinar\Dropbox\Creación de MOCs\MOC Dash Python\Datasets\3.11\PEATONES_2020_mod.csv',encoding = 'ISO-8859-1',delimiter=';')

#hist_data y group_labels para pregunta 1
#hist_data = [df_peatones["PEATONES"]]
#group_labels = ["Tráfico peatonal"]

#hist_data y group_labels para pregunta 2

#Creación de trazas independientes para cada distrito objetivo
trace0 = df_peatones[df_peatones["DISTRITO"]=="Arganzuela"]["PEATONES"]
trace1 = df_peatones[df_peatones["DISTRITO"]=="Centro"]["PEATONES"]
hist_data = [trace0, trace1]
group_labels = ["Arganzuela", "Centro"]

#Creación de la figura indicando el tamaño del bin (bin_size) igual a 10
fig = ff.create_distplot(hist_data, group_labels,bin_size=10)
#Generación del plot a partir de la figura definida y nombre del fichero de salida HTML
pyo.plot(fig, filename="3.11_Ej_Distplot.html")
