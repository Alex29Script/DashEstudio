#Importación de librerías
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

#Carga de datos
df_pp = pd.read_excel(r'C:\Users\ivan_pinar\Dropbox\Creación de MOCs\MOC Dash Python\Datasets\3.13\Peatones_prom_coord.xlsx')
#Definimos la cadena con el token de la cuenta de mapbox
mapbox_access_token = "pk.eyJ1IjoiaXZhbmxvc2FyIiwiYSI6ImNrZTJpdWN0NDA5cXUyem1oOGx3NGh1bGsifQ.wuhB2vmk4QGrciFWYygqaA"#open(".mapbox_token").read()

#Creamos directamente la figura, obviamos data puesto que directamente lo definimos como el primer argumento de Figure
fig = go.Figure(go.Scattermapbox(
        lon = df_pp['LONGITUD'], #Seleccionamos nuestra columna con la coordenada longitud
        lat = df_pp['LATITUD'], #Seleccionamos nuestra columna con la coordenada latitud
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=df_pp["Peatones_prom"]/10, #Indicamos que el tamaño dependa del tráfico promedio de peatones y escalamos entre 10 para no inundar el mapa
            color=df_pp["Peatones_prom"] #Indicamos que el color dependa del tráfico promedio de peatones (podemos usar otra variable)
        )
    ))

#Actualizamos la propiedad "layout" de la figura
fig.update_layout(
    autosize=True,
    hovermode='closest', #muestra el dato más cercano al mover el cursor por el gráfico
    mapbox=dict(
        accesstoken=mapbox_access_token,
        center=dict(
            lat=40.41, #coordenadas del centro de nuestro mapa inicial
            lon=-3.7 #coordenadas del centro de nuestro mapa inicial
        ),
        zoom=12 #zoom inicial del mapa
    ),
)

pyo.plot(fig, filename="3.13 Geomap peatones_s.html")
