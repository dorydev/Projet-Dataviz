#Import library
import dash_bootstrap_components as dbc
from dash import html

GIT_URL = "https://github.com/dorydev/Projet-DataViz" #url du repository

navbar = dbc.Navbar(
    [
        html.A(
            dbc.Row (
                [
                    html.Div([], className="invisible-item"),
                    html.Div([
                        #dbc.NavLink("Home", href="/home", className="nav-link"),
                        dbc.NavLink("Dashboard", href="/dashboard", className="nav-link"),
                        #dbc.NavLink("Upload Data", href="/upload_data", className="nav-link"),
                        dbc.NavLink(
                            [
                                "GitHub",
                                html.Img(src="assets/img/logo.png", className="github-icon"),
                                
                            ],
                            href=GIT_URL,
                            className="nav-link",
                        ),
                    ], className="align-navbar-items"),
                    html.Div([], className="invisible-item")
                ],
                align="center",
                className="navbar-items",
            ),
        )
    ],
)

layout_navbar = html.Header([navbar]) #export "layout-navbar"

