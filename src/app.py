import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from Pages import home, stress, sleep, oxygen, weather, modelo, landingpage, creador
import assets

# Inicializar la app con Bootstrap y estilos
app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Proyecto Final"
server = app.server

# Layout base
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dbc.NavbarSimple(
        children=[
            dbc.NavItem(dcc.Link("Home", href="/", className="nav-link")),
            dbc.DropdownMenu(
                label="Páginas Detalladas",
                children=[
                    dbc.DropdownMenuItem("Estrés", href="/stress"),
                    dbc.DropdownMenuItem("Sueño", href="/sleep"),
                    dbc.DropdownMenuItem("Oxígeno Saturación", href="/oxygen"),
                    dbc.DropdownMenuItem("Clima", href="/weather"),
                ],
                nav=True,
                in_navbar=True,
            ),
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
    elif pathname == '/stress':
        return stress.layout
    elif pathname == '/sleep':
        return sleep.layout
    elif pathname == '/oxygen':
        return oxygen.layout
    elif pathname == '/weather':
        return weather.layout
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
