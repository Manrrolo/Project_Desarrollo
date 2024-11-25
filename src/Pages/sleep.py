from dash import dcc, html
import plotly.express as px
from data_processing import load_and_clean_data

# Cargar datos
data = load_and_clean_data(
    "./Data/filtered_cleaned_com.samsung.shealth.sleep_combined.20241124164179_processed.csv"
)

# Extraer DataFrame
sleep_data = data["filtered_cleaned_com.samsung.shealth.sleep_combined.20241124164179_processed.csv"]

# Crear gráficos
sleep_boxplot = px.box(
    sleep_data,
    x='efficiency',
    y='sleep_score',
    title='Distribución de Eficiencia vs Puntaje de Sueño',
    labels={'efficiency': 'Eficiencia', 'sleep_score': 'Puntaje de Sueño'}
)

sleep_scatter = px.scatter(
    sleep_data,
    x='timestamp',
    y='sleep_duration',
    title='Duración de Sueño en el Tiempo',
    labels={'timestamp': 'Fecha', 'sleep_duration': 'Duración de Sueño (minutos)'}
)

sleep_histogram = px.histogram(
    sleep_data,
    x='sleep_duration',
    title='Distribución de Duración de Sueño',
    labels={'sleep_duration': 'Duración de Sueño (minutos)'}
)

sleep_efficiency = px.scatter(
    sleep_data,
    x='sleep_duration',
    y='efficiency',
    title='Relación entre Duración de Sueño y Eficiencia',
    labels={'sleep_duration': 'Duración de Sueño (minutos)', 'efficiency': 'Eficiencia'}
)

# Layout
layout = html.Div([
    html.H2("Análisis de Sueño"),
    html.Div(className="row", children=[
        html.Div(className="col", children=[dcc.Graph(figure=sleep_boxplot)]),
        html.Div(className="col", children=[dcc.Graph(figure=sleep_scatter)]),
    ]),
    html.Div(className="row", children=[
        html.Div(className="col", children=[dcc.Graph(figure=sleep_histogram)]),
        html.Div(className="col", children=[dcc.Graph(figure=sleep_efficiency)]),
    ])
])
