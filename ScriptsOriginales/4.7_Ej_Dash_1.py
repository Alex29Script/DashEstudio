import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash()

# Carga datos
df_sp500 = pd.read_csv(r'C:\Users\ivan_pinar\Dropbox\Creación de MOCs\MOC Dash Python\Datasets\4.7\SP500_data_.csv',encoding = 'ISO-8859-1',delimiter=',')

#Objetos plotly.graph
data1 = [go.Scatter(x=df_sp500["Date"],
                    y=df_sp500["Close"],
                    mode="lines")]

layout1 = go.Layout(title="SP500 Cotización",
                    xaxis=dict(title="Fecha"),
                    yaxis=dict(title="SP500 valor"))

data2 = [go.Bar(x=df_sp500["Date"],
                    y=df_sp500["Volume"])]

layout2 = go.Layout(title="SP500 Volumen negociado",
                    xaxis=dict(title="Fecha"),
                    yaxis=dict(title="Volumen"))

#Definición del layout de la app a partir de componentes HTML y Core
app.layout = html.Div([
                    html.Label('Selección'), #Cadena de texto antes del dropdown
                    dcc.Dropdown( #Creación componente dropdown
                        options=[
                            {'label': 'Apertura', 'value': 'Open'}, #la propiedad value es la utilizada internamente en el script
                            {'label': 'Cierre', 'value': 'Close'},
                        ],
                        value='Close'
                    ),
                    dcc.Graph(id='lineplot', #Creación componente Graph 1
                    figure = {'data':data1,
                            'layout':layout1}
                    ),
                    dcc.Graph(id='barplot', #Creación componente Graph 2
                    figure = {'data':data2,
                            'layout':layout2}
                                    )])

#Sentencias para abrir el servidor al ejecutar este script
if __name__ == '__main__':
    app.run_server(port=7000)
