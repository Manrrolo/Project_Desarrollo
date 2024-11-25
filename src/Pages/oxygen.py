from dash import dcc, html
import plotly.express as px
from data_processing import load_and_clean_data

# Cargar datos
data = load_and_clean_data(
    "./Data/filtered_cleaned_com.samsung.health.oxygen_saturation.raw.20241124164179_processed.csv"
)

# Extraer DataFrame
oxygen_data = data["filtered_cleaned_com.samsung.health.oxygen_saturation.raw.20241124164179_processed.csv"]

# Crear gráficos
oxygen_boxplot = px.box(
    oxygen_data,
    x='channel',
    y='time',
    title='Distribución del Tiempo por Canal de Oxígeno',
    labels={'channel': 'Canal', 'time': 'Tiempo (s)'}
)

oxygen_histogram = px.histogram(
    oxygen_data,
    x='time',
    title='Distribución del Tiempo de Saturación de Oxígeno',
    labels={'time': 'Tiempo (s)'}
)

oxygen_scatter = px.scatter(
    oxygen_data,
    x='timestamp',
    y='time',
    color='channel',
    title='Tiempo por Canal en el Tiempo',
    labels={'timestamp': 'Fecha', 'time': 'Tiempo (s)', 'channel': 'Canal'}
)

oxygen_trend = px.line(
    oxygen_data,
    x='timestamp',
    y='time',
    color='channel',
    title='Tendencia de Tiempo de Oxígeno por Canal',
    labels={'timestamp': 'Fecha', 'time': 'Tiempo (s)', 'channel': 'Canal'}
)

# Layout
layout = html.Div([
    html.H2("Análisis de Saturación de Oxígeno"),
    html.Div(className="row", children=[
        html.Div(className="col", children=[dcc.Graph(figure=oxygen_boxplot)]),
        html.Div(className="col", children=[dcc.Graph(figure=oxygen_scatter)]),
    ]),
    html.Div(className="row", children=[
        html.Div(className="col", children=[dcc.Graph(figure=oxygen_histogram)]),
        html.Div(className="col", children=[dcc.Graph(figure=oxygen_trend)]),
    ])
])
