#Importación de librerías
import dash
import dash_core_components as dcc
import dash_html_components as html

#Creación de la app de dash
app = dash.Dash()

#Definición diccionario de los colores utilizados en la app para homogeneidad
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

#Definición del layout de la app a partir de componentes HTML y Core
app.layout = html.Div(children=[
    html.H1(children='Primer Dashboard con Dash',
            style={ #Definición del estilo del componente H1
                'textAlign': 'center',
                'color': colors['text']
    }),
    html.Div(children='Dash: Framework para aplicaciones web con Python',
             style={ #Definición del estilo del componente Div interno
                    'textAlign': 'center',
                    'color': colors['text']}
            ),

    dcc.Graph(
        id='ejemplo',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 8, 2], 'type': 'bar', 'name': 'MA'},
                {'x': [1, 2, 3], 'y': [3, 4, 5], 'type': 'bar', 'name': 'BA'},
            ],
            'layout': {
                'title': 'Comparativa Madrid - Barcelona',
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {'color': colors['text']}
            }
        }
    )
],
    style={'backgroundColor': colors['background']} #Definición del estilo del componente Div externo (global)
)

#Sentencias para abrir el servidor al ejecutar este script
if __name__ == '__main__':
    app.run_server(port=8000)
