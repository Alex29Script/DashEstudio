import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import pandas as pd
import dash_auth

LISTA_USUARIOS = [["Juan","007"],["Laura","200"]]

app = dash.Dash()
auth = dash_auth.BasicAuth(app,LISTA_USUARIOS)
server = app.server

mapbox_access_token = "pk.eyJ1IjoiaXZhbmxvc2FyIiwiYSI6ImNrZTJpdWN0NDA5cXUyem1oOGx3NGh1bGsifQ.wuhB2vmk4QGrciFWYygqaA"

# CARGA DE DATOS
df_ventas = pd.read_excel('Ventas.xlsx',sheet_name="Detalle") #Especificar el fichero sin ruta, en Heroku es la ruta inicial donde se sube el fichero
df_ventas_acum = pd.read_excel('Ventas.xlsx',sheet_name="Acumulado") #Especificar el fichero sin ruta, en Heroku es la ruta inicial donde se sube el fichero

# DEFINIR FIGURA ESTÁTICA PARA VENTAS GEOGRÁFICAS
fig_mapa = go.Figure(go.Scattermapbox(
        lon = df_ventas_acum['Longitud'],
        lat = df_ventas_acum['Latitud'],
        mode='markers',
        text= df_ventas_acum['Suma Ingresos'],
        marker=go.scattermapbox.Marker(
            size=df_ventas_acum['Suma Ingresos']/50000,
            color=df_ventas_acum['Suma Ingresos']/50000
        )
    ))

fig_mapa.update_layout(
    autosize=True,
    hovermode='closest',
    mapbox=dict(
        accesstoken=mapbox_access_token,
        bearing=0,
        center=dict(
            lat=40.41,
            lon=-3.7
        ),
        pitch=0,
        zoom=2
    ),
)

# DEFINICIÓN LAYOUT
app.layout = html.Div([
                    html.Div([
                    html.Label('País'),
                    dcc.Dropdown(id='selector',
                        options=[{'label': i, 'value': i} for i in df_ventas['País'].unique()],
                        value='Spain'
                    )],style={'width': '48%', 'display': 'inline-block'}),

                    html.Div([
                    html.Label('Rango fechas'),
                    dcc.DatePickerRange(id='selector_fecha',start_date=df_ventas["Fecha compra"].min(),end_date=df_ventas["Fecha compra"].max())
                    ],style={'width': '48%', 'float': 'right', 'display': 'inline-block'}),



                    html.Div([
                    dcc.Graph(id='barplot_ventas_seg')
                    ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),

                    html.Div([
                    dcc.Graph(id='barplot_beneficio_cat')
                    ],style={'width': '33%', 'float': 'center', 'display': 'inline-block'}),

                    html.Div([
                    dcc.Graph(id='lineplot_cantidad')
                    ],style={'width': '33%', 'float': 'right', 'display': 'inline-block'}),

                    html.Div([
                    dcc.Graph(id='mapa_ventas', figure=fig_mapa)
                    ],style={'width': '100%'})

                    ])

# CREACIÓN DE GRÁFICOS E INTERACTIVIDAD
#Callback para actualizar gráfico de Segmento en función del dropdown de País y según selector de fechas
@app.callback(Output('barplot_ventas_seg', 'figure'),
              [Input('selector_fecha', 'start_date'),Input('selector_fecha', 'end_date'),Input('selector', 'value')])
def actualizar_graph_seg(fecha_min, fecha_max, seleccion):
    filtered_df = df_ventas[(df_ventas["Fecha compra"]>=fecha_min) & (df_ventas["Fecha compra"]<=fecha_max) & (df_ventas["País"]==seleccion)]

    df_agrupado = filtered_df.groupby("Segmento")["Importe"].agg("sum").to_frame(name = "Ingresos").reset_index()

    return{
        'data': [go.Bar(x=df_agrupado["Segmento"],
                            y=df_agrupado["Ingresos"]
                            )],
        'layout': go.Layout(
            title="¿Cuáles han sido las ventas en cada segmento de clientes?",
            xaxis={'title': "Segmento"},
            yaxis={'title': "Ingresos totales"},
            hovermode='closest'
        )}


#Callback para actualizar gráfico de beneficio de categorías en función del dropdown de País y según selector de fechas
@app.callback(Output('barplot_beneficio_cat', 'figure'),
              [Input('selector_fecha', 'start_date'),Input('selector_fecha', 'end_date'),Input('selector', 'value'),Input('barplot_ventas_seg', 'hoverData')])
def actualizar_graph_cat(fecha_min, fecha_max, seleccion,hoverData):

    v_index = hoverData['points'][0]['x']
    filtered_df = df_ventas[(df_ventas["Fecha compra"]>=fecha_min) & (df_ventas["Fecha compra"]<=fecha_max) & (df_ventas["País"]==seleccion) & (df_ventas["Segmento"]==v_index)]

    df_agrupado = filtered_df.groupby("Categoría")["Beneficio"].agg("sum").to_frame(name = "Beneficio").reset_index()

    return{
        'data': [go.Bar(x=df_agrupado["Categoría"],
                            y=df_agrupado["Beneficio"]
                            )],
        'layout': go.Layout(
            title="¿Cuáles han sido los beneficios de cada categoría?",
            xaxis={'title': "Categoría"},
            yaxis={'title': "Beneficios totales"},
            hovermode='closest')}


#Callback para actualizar gráfico de evolución cantidad de pedido en función del dropdown de País y según selector de fechas
@app.callback(Output('lineplot_cantidad', 'figure'),
              [Input('selector_fecha', 'start_date'),Input('selector_fecha', 'end_date'),Input('selector', 'value'),Input('barplot_ventas_seg', 'hoverData')])
def actualizar_graph_cat(fecha_min, fecha_max, seleccion,hoverData):

    v_index = hoverData['points'][0]['x']
    filtered_df = df_ventas[(df_ventas["Fecha compra"]>=fecha_min) & (df_ventas["Fecha compra"]<=fecha_max) & (df_ventas["País"]==seleccion) & (df_ventas["Segmento"]==v_index)]

    df_agrupado = filtered_df.groupby("Fecha compra")["Cantidad"].agg("sum").to_frame(name = "Cantidad").reset_index()

    return{
        'data': [go.Scatter(x=df_agrupado["Fecha compra"],
                            y=df_agrupado["Cantidad"],
                            mode="lines+markers"
                            )],
        'layout': go.Layout(
            title="¿Cuál es la evolución de la cantidad de pedidos solicitados?",
            xaxis={'title': "Fecha"},
            yaxis={'title': "Cantidad"},
            hovermode='closest')}



if __name__ == '__main__':
    app.run_server()
