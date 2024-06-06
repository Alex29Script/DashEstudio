#Definición de librerías
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output #Módulos de interactividad Input, Output

app = dash.Dash()

#Definición del layout de la app a partir de componentes HTML y Core
app.layout = html.Div([
    dcc.Input(id='mi-input', value='Valor inicial', type='text'), #Componente Core de tipo Input, no confundir con la librería importada
    html.Div(id='mi-div')
])

# CREACIÓN DE INTERACTIVIDAD
#Callback para actualizar texto del div en función del input mi-input
@app.callback(
    Output(component_id='mi-div', component_property='children'),
    [Input(component_id='mi-input', component_property='value')]
)
def actualizar_div(valor_entrada):
    return 'Has insertado la cadena: "{}"'.format(valor_entrada)

#Sentencias para abrir el servidor al ejecutar este script
if __name__ == '__main__':
    app.run_server(port=8010)
