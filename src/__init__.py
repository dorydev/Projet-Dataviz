#Import library
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
#import pages
from pages.header import layout_navbar
from pages.dashboard import layout_dashboard
#Autres pages
#from pages.home import layout_home
#from pages.upload_data import layout_upload 
from app import app, server


#Principal layout de l'app
app.layout = html.Div([
    layout_navbar, #ne pas oublier, sous peine de header inexistant /!\
    dcc.Location(id='url', refresh=True),
    html.Div(id='page-content')
], className="container")

#Récupère les pages dans  le dossier : /pages pour les link entre elles
@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_pages(pathname):
    #if pathname == '/' or pathname == '/home': -> pour ajouter une homepage
    #    return layout_home
    if pathname == '/' or pathname == '/dashboard': #-> main page du projet
        return layout_dashboard
    #elif pathname == "/upload_data":
    #    return layout_upload

#Fonction principale, c'est magique !
if __name__ == '__main__':
    app.run_server(debug=True)