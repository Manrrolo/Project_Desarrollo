
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from Pages import home, modelo, landingpage, creador
import assets

# Inicializar la app con los estilos personalizados y Bootstrap
app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Proyecto Final"

# Layout base
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dbc.NavbarSimple(
        children=[
            dbc.NavItem(dcc.Link("Home", href="/", className="nav-link")),
            dbc.NavItem(dcc.Link("Modelo", href="/modelo", className="nav-link")),
            dbc.NavItem(dcc.Link("Landing Page", href="/landingpage", className="nav-link")),
            dbc.NavItem(dcc.Link("Nosotros", href="/creador", className="nav-link")),
        ],
        brand="Proyecto Final",
        color="dark",
        dark=True,
        fixed="top"
    ),
    html.Div(id='page-content', style={'margin-top': '70px'})  # Espaciado para la navbar
])

# Callbacks para el ruteo
@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    if pathname == '/':
        return home.layout
    elif pathname == '/modelo':
        return modelo.layout
    elif pathname == '/landingpage':
        return landingpage.layout
    elif pathname == '/creador':
        return creador.layout
    else:
        return html.H1("404: Página no encontrada", style={'textAlign': 'center'})

if __name__ == '__main__':
    app.run_server(debug=True)
