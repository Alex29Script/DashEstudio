# FASE 1: IMPORTAR LIBRERÍAS
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import pandas as pd

app = dash.Dash()

# FASE 1: CARGA DE DATOS (dataframe df_ventas --> Pestaña "Detalle" / dataframe df_ventas_acum --> Pestaña "Acumulado")
df_ventas = pd.read_excel(...)
df_ventas_acum = pd.read_excel(...)

# FASE 3: CREACIÓN GRÁFICO GEOGRÁFICO
mapbox_access_token = "..."
# DEFINIR FIGURA ESTÁTICA PARA VENTAS GEOGRÁFICAS
fig_mapa = go.Figure(go.Scattermapbox(...





        )
    ))

fig_mapa.update_layout(...





    ),
)

# FASE 1: DEFINICIÓN LAYOUT
app.layout = html.Div([
                    html.Div([
                    html.Label('País'),
                    dcc.Dropdown(...




                    )],style={'width': '48%', 'display': 'inline-block'}),

                    html.Div([
                    html.Label('Rango fechas'),
                    dcc.DatePickerRange(...




                    )
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

# FASE 4: Callback para actualizar gráfico de Segmento en función del dropdown de País y según selector de fechas
@app.callback(Output(...),
              [Input(...])
def actualizar_graph_seg(fecha_min, fecha_max, seleccion):
    filtered_df = ...

# FASE 2: CREACIÓN DE GRÁFICOS Y GROUPBY (considerar que tenemos un dataframe ya filtrado filtered_df)
    df_agrupado = filtered_df.groupby("Segmento")["Importe"].agg("sum").to_frame(name = "Ingresos").reset_index()

    return{
        'data': ...,

        'layout': ...
        )}

# FASE 4: Callback para actualizar gráfico de beneficio de categorías en función del dropdown de País y según selector de fechas
@app.callback(Output(...),
              [Input(...)])
def actualizar_graph_cat(fecha_min, fecha_max, seleccion,hoverData):
# FASE 5: Interactividad inter-gráfico hoverData
    v_index = hoverData['points'][0]['x']
    filtered_df = ...

# FASE 2: CREACIÓN DE GRÁFICOS Y GROUPBY (considerar que tenemos un dataframe ya filtrado filtered_df)
    df_agrupado = ...

    return{
        'data': ...,
        'layout': ...

#FASE 4: Callback para actualizar gráfico de evolución cantidad de pedido en función del dropdown de País y según selector de fechas
@app.callback(Output(...),
              [Input(...)])
def actualizar_graph_cat(fecha_min, fecha_max, seleccion,hoverData):
# FASE 5: Interactividad inter-gráfico hoverData
    v_index = hoverData['points'][0]['x']
    filtered_df = ...

# FASE 2: CREACIÓN DE GRÁFICOS Y GROUPBY (considerar que tenemos un dataframe ya filtrado filtered_df)
    df_agrupado = ...

    return{
        'data': ...,
        'layout': ...



if __name__ == '__main__':
    app.run_server()
