#Importar librerías
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash()

# Carga datos
df_sp500 = pd.read_csv(r'...',encoding = 'ISO-8859-1',delimiter=',')

#Objetos plotly.graph
data1 = [go.Scatter(...)]

layout1 = go.Layout(...)

data2 = [go.Bar(...)]

layout2 = go.Layout(...)

#Definición del layout de la app a partir de componentes HTML y Core
app.layout = html.Div([
                    ...





                    ])

#Sentencias para abrir el servidor al ejecutar este script
if __name__ == '__main__':
    app.run_server()
