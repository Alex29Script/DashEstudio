#Importación de librerías
import plotly.offline as pyo
import plotly.figure_factory as ff #Nueva librería para gráficos complejos
import pandas as pd

#Carga de datos
df_peatones = pd.read_csv(r'...',encoding = 'ISO-8859-1',delimiter=';')



#hist_data y group_labels para pregunta 1
hist_data = [...]
group_labels = [...]

#hist_data y group_labels para pregunta 2
#Creación de trazas independientes para cada distrito objetivo
#trace0 = ...
#trace1 = ...
#hist_data = [trace0, trace1]
#group_labels = ["Arganzuela", "Centro"]

#Creación de la figura indicando el tamaño del bin (bin_size) igual a 10
fig = ff.create_distplot(...)
#Generación del plot a partir de la figura definida y nombre del fichero de salida HTML
pyo.plot(...)
