#Importar librerías
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import json #librería para retornar información en formato json

app = dash.Dash()

# CARGA DE DATOS
df_temp = pd.read_excel(r'C:\Users\ivan_pinar\Dropbox\Creación de MOCs\MOC Dash Python\Datasets\5.6\Temperaturas.xlsx')

#Creación trazas de datos para cada ciudad
traces = []
for nombre_ciudad in df_temp["Ciudad"].unique():
    df_ciudad = df_temp[df_temp['Ciudad'] == nombre_ciudad]
    traces.append(go.Scatter(
        x=df_ciudad["FECHA"],
        y=df_ciudad["T_Promedio"],
        text=df_ciudad["Ciudad"],
        mode='markers+lines',
        opacity=0.7,
        marker={'size': 5},
        name=nombre_ciudad
    ))

app.layout = html.Div([
    html.Div([
    dcc.Graph(
        id='temp_plot',
        figure={
            'data': traces,
            'layout': go.Layout(
                xaxis={'title': 'Fecha'},
                yaxis={'title': 'Temperatura media'},
                hovermode='closest'
            )
        }
    )], style={'width':'50%', 'float':'left'}),

    html.Div([
    html.Pre(id='hover-data', style={'paddingTop':35}) #Elemento HTML Pre (preformateado) conserva espacios y saltos de línea
    ], style={'width':'30%'})
])

# CREACIÓN DE INTERACTIVIDAD
#Callback para devolver en componente Pre hover-data la información en formato json respecto a dónde tengamos el cursor en temp_plot
@app.callback(
    Output('hover-data', 'children'),
    [Input('temp_plot', 'hoverData')]) #poder usar las propiedades hoverData, clickData o selectedData
def callback_json(hoverData):
    return json.dumps(hoverData, indent=2) #Información json con propiedades de hoverData

#Sentencias para abrir el servidor al ejecutar este script
if __name__ == '__main__':
    app.run_server(port=8000)
