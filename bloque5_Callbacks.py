import dash
from dash import dcc # contiene los componentes como graficos
from dash import html # contiene los elementos html, usa React
# importante The dash_core_components package is deprecated. Please replace
import plotly.graph_objects as go
import pandas as pd

from dash.dependencies import Input, Output #31


df_temp=pd.read_excel("./Datasets/5.2/Temperaturas.xlsx")



app=dash.Dash()


# Callbacks: interaccion para conectar los componentes del dashboard

#31. Callbacks sencillo


app.layout=html.Div(
    [
        dcc.Input(id="input_1", value="Valor inicial", type="text"),
        html.H3(id="salida"),
        dcc.Graph(id="g_lineas"),
        dcc.DatePickerRange(id="selector_fecha", start_date=df_temp["FECHA"].min(),end_date=df_temp["FECHA"].max())
        
    ]
)



@app.callback(
        Output("salida", "children"),# id, propiedad a modificar
        [Input("input_1", "value")] # id, propiedad a leer
)
def actualizar_dev(valor_entrada):
    return "Haz insertado '{}'".format(valor_entrada)

# 32 callback con graficos
@app.callback(
        Output("g_lineas", "figure"),
        [Input("selector_fecha","start_date"),Input("selector_fecha","end_date")]
)
def actualizar_grafico(fecha_min, fecha_max):
    filtered_df=df_temp[(df_temp["FECHA"]>=fecha_min)&(df_temp["FECHA"]<=fecha_max)]
    traces=[]
    for nombre_ciudad in filtered_df["Ciudad"].unique():
        df_ciudad=filtered_df[filtered_df["Ciudad"]==nombre_ciudad]
        traces.append(go.Scatter(
            x=df_ciudad["FECHA"],
            y=df_ciudad["T_Promedio"],
            text=df_ciudad["Ciudad"],
            mode="lines",
            opacity=0.7,
            marker={"size":15},
            name=nombre_ciudad
        ))
    return {
        "data":traces,
        "layout":go.Layout(
            xaxis={"title":"Fecha"},
            yaxis={"title":"Temperatura media"},
            hovermode="closest"
        )
    }












if __name__=="__main__":
    app.run_server(debug=True)