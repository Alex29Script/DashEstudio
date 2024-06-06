#Importación de librerías
import plotly.offline as pyo
import plotly.figure_factory as ff #Nueva librería para gráficos complejos
import numpy as np

#Creación de datos aleatorios con numpy randn --> 2 arrays x1 / x2
x1 = np.random.randn(1000) #array con 1000 valores aleatorios con media 0 y varianza 1
x2 = np.random.randn(1000)+2 #array con 1000 valores aleatorios con media 2 y varianza 1

#Objeto hist_data con los datos a utilizar, pueden ser columnas de un dataframe
hist_data = [x1,x2]
#Etiquetas utilizadas para cada distribución de datos
group_labels = ["Distribución x1","Distribución x2"]

#Creación de la figura indicando el tamaño del bin (bin_size) de cada distribución
fig = ff.create_distplot(hist_data, group_labels, bin_size=[2,2])
#Generación del plot a partir de la figura definida y nombre del fichero de salida HTML
pyo.plot(fig, filename="3.10 Distplot.html")
