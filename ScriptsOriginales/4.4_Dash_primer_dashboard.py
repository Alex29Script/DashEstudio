#Importación de librerías
import dash
import dash_core_components as dcc
import dash_html_components as html

#Creación de la app de dash
app = dash.Dash()

#Definición del layout de la app a partir de componentes HTML y Core
app.layout = html.Div([ #Es es el div global de nuestra app
    html.H1(children='Primer Dashboard con Dash'), #Elemento cabecera de texto H1
    html.Div(children='Dash: Framework para aplicaciones web con Python.'),

    dcc.Graph( #Elemento gráfico de librería Core insertado en el Div global
        id='ejemplo',
        figure={
            'data': [ #objeto de datos para crear la figura de Plotly
                {'x': [1, 2, 3], 'y': [4, 8, 2], 'type': 'bar', 'name': 'MA'},
                {'x': [1, 2, 3], 'y': [3, 4, 5], 'type': 'bar', 'name': 'BA'},
            ],
            'layout': {  #objeto layout para crear la figura de Plotly
                'title': 'Comparativa Madrid - Barcelona'
            }
        }
    )
])

#Sentencias para abrir el servidor al ejecutar este script
if __name__ == '__main__':
    app.run_server()
