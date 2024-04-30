
#---------------------------------------#
#                                       #
#                                       #
#                                       #
#                                       #
#                                       #
#                                       #
#---------------------------------------#

#Import library
from dash import Dash, dcc, html, dash_table, Input, Output, State, callback
import dash_bootstrap_components as dbc

app = Dash(__name__)#ne pas rajouter "external_stylesheets=[dbc.themes.BOOTSTRAP]"
                    #à vos risques et périls....

server = app.server #server init
app.config.suppress_callback_exceptions = True #parametre de config de l'app
