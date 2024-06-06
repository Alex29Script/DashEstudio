#Importación de librerías
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

#Creación de la app de dash
app = dash.Dash()

# Carga datos
df_iris = pd.read_csv(r'C:\Users\ivan_pinar\Dropbox\Creación de MOCs\MOC Dash Python\Datasets\4.6\iris_dataset.csv',encoding = 'ISO-8859-1',delimiter=',')

#Objetos plotly.graph
data1 = [go.Scatter(x=df_iris["longitud_sépalo"],
                    y=df_iris["anchura_sépalo"],
                    mode="markers",
                    marker = dict(
                            size=12,
                            symbol="circle",
                            line={"width":3} #línea del marcador
                    ))]

layout1 = go.Layout(title="Iris Scatter plot sépalo",
                    xaxis=dict(title="Longitud sépalo"),
                    yaxis=dict(title="Anchura sépalo"))

data2 = [go.Scatter(x=df_iris["longitud_pétalo"],
                    y=df_iris["anchura_pétalo"],
                    mode="markers",
                    marker = dict(
                            size=12,
                            symbol="circle",
                            line={"width":3} #línea del marcador
                    ))]

layout2 = go.Layout(title="Iris Scatter plot pétalo",
                    xaxis=dict(title="Longitud pétalo"),
                    yaxis=dict(title="Anchura pétalo"))

#Definición del layout de la app a partir de componentes HTML y Core
app.layout = html.Div([dcc.Graph(id='scatterplot',
                    figure = {'data':data1,
                            'layout':layout1}
                    ),
                    dcc.Graph(id='scatterplot2',
                    figure = {'data':data2,
                            'layout':layout2}
                              )
                    ])

#Sentencias para abrir el servidor al ejecutar este script
if __name__ == '__main__':
    app.run_server(port=8000)
