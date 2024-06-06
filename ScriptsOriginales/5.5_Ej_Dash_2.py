#Importar librerías
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import pandas as pd

app = dash.Dash()

# CARGA DE DATOS
df_sp500 = pd.read_csv(r'C:\Users\ivan_pinar\Dropbox\Creación de MOCs\MOC Dash Python\Datasets\5.5\SP500_data_.csv',encoding = 'ISO-8859-1',delimiter=',')

# DEFINICIÓN LAYOUT
app.layout = html.Div([
                    html.Div([
                    html.Label('Selección'),
                    dcc.Dropdown(id='selector',
                        options=[
                            {'label': 'Apertura', 'value': 'Open'},
                            {'label': 'Cierre', 'value': 'Close'},
                        ],
                        value='Close'
                    )],style={'width': '48%', 'display': 'inline-block'}),

                    html.Div([
                    html.Label('Rango fechas'),
                    dcc.DatePickerRange(id='selector_fecha',start_date=df_sp500["Date"].min(),end_date=df_sp500["Date"].max()),
                    ],style={'width': '48%', 'float': 'right', 'display': 'inline-block'}),

                    dcc.Graph(id='lineplot'),

                    dcc.Graph(id='barplot')])

# CREACIÓN DE GRÁFICOS E INTERACTIVIDAD
#Callback para actualizar gráfico de cotización en función del dropdown eligiendo apertura o cierre de sesión y según selector de fechas
@app.callback(Output('lineplot', 'figure'),
              [Input('selector_fecha', 'start_date'),Input('selector_fecha', 'end_date'),Input('selector', 'value')])
def actualizar_graph_line(fecha_min, fecha_max, seleccion):
    filtered_df = df_sp500[(df_sp500["Date"]>=fecha_min) & (df_sp500["Date"]<=fecha_max)]

    if seleccion == "Open":
        return{
            'data': [go.Scatter(x=filtered_df["Date"],
                                y=filtered_df["Open"],
                                mode='lines'
                                )],
            'layout': go.Layout(
                title="SP500 Cotización",
                xaxis={'title': "Fecha"},
                yaxis={'title': "Valor cotización a apertura"},
                hovermode='closest'
            )}

    else:
        return{
            'data': [go.Scatter(x=filtered_df["Date"],
                                y=filtered_df["Close"],
                                mode="lines")],
            'layout': go.Layout(
                title="SP500 Cotización",
                xaxis={'title': "Fecha"},
                yaxis={'title': "Valor cotización a cierre"},
                hovermode='closest'
                )
    }

#Callback para actualizar gráfico de volumen según selector de fechas
@app.callback(Output('barplot', 'figure'),
              [Input('selector_fecha', 'start_date'),Input('selector_fecha', 'end_date')])
def actualizar_graph_bar(fecha_min, fecha_max):
    filtered_df = df_sp500[(df_sp500["Date"]>=fecha_min) & (df_sp500["Date"]<=fecha_max)]
    return{
        'data': [go.Bar(x=filtered_df["Date"],
                        y=filtered_df["Volume"])],

        'layout': go.Layout(title="SP500 Volumen negociado",
                        xaxis=dict(title="Fecha"),
                        yaxis=dict(title="Volumen"))
            }

#Sentencias para abrir el servidor al ejecutar este script
if __name__ == '__main__':
    app.run_server()
