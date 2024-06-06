import dash
from dash import dcc # contiene los componentes como graficos
from dash import html # contiene los elementos html, usa React
# importante The dash_core_components package is deprecated. Please replace
import plotly.graph_objects as go
import pandas as pd



app=dash.Dash()

df_iris=pd.read_csv("./Datasets/4.6/iris_dataset.csv",encoding="ISO-8859-1", delimiter=",")


data_iris=[
    go.Scatter(
        x=df_iris["longitud_sépalo"],
        y=df_iris["anchura_sépalo"],
        mode="markers",
        marker=dict(
            size=12,
            symbol="circle",
            line={"width":3}
        )
    )
]

layyout_irirs=go.Layout(
    title="Iris de sépalo",
    xaxis=dict(title="longitud"),
    yaxis=dict(title="Anchura")
)







app.layout=html.Div(# el layout contiene una lista de todos los objetos html
    [
        html.H1(children="Primer Dashboard con Dash Python"), 
        html.Div(children="Dash es una framework para aplicaciones web"),
        dcc.Graph(
            id="fig_ini",
            figure={
                "data":[
                    {
                        "x":[1,2,3], "y":[5,8,3], "type":"bar","name":"Madrid"
                    },
                    {
                        "x":[1,2,3], "y":[3,6,8], "type":"bar","name":"Barcelona"
                    },

                ],
                "layout":{
                    "title":"Comparativa"
                }
            }
        ),
        dcc.Graph(
            id="iris_grafico",
            figure={
                "data":data_iris,
                "layout":layyout_irirs
            }
        )

    ]
)

#clase 29
# https://www.udemy.com/course/master-dashboards-interactivos-con-python-dash-plotly/learn/lecture/21877552#content




if __name__=="__main__":
    app.run_server(debug=True)