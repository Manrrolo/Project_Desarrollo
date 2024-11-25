from dash import dcc, html
import plotly.express as px
from data_processing import load_and_clean_data

# Cargar datos
data = load_and_clean_data(
    "./Data/filtered_cleaned_com.samsung.shealth.activity.day_summary.20241124164179_processed.csv"
)

# Extraer DataFrame
activity_data = data["filtered_cleaned_com.samsung.shealth.activity.day_summary.20241124164179_processed.csv"]

# Crear gráficos
activity_calories = px.bar(
    activity_data,
    x='timestamp',
    y='calories',
    title='Calorías Quemadas por Día',
    labels={'timestamp': 'Fecha', 'calorie': 'Calorías'}
)

activity_steps = px.line(
    activity_data,
    x='timestamp',
    y='step_count',
    title='Pasos Diarios',
    labels={'timestamp': 'Fecha', 'step_count': 'Cantidad de Pasos'}
)

activity_active_time = px.scatter(
    activity_data,
    x='timestamp',
    y='active_time',
    title='Tiempo Activo por Día',
    labels={'timestamp': 'Fecha', 'active_time': 'Tiempo Activo (minutos)'}
)

activity_goal = px.histogram(
    activity_data,
    x='goal',
    title='Distribución de Metas Diarias',
    labels={'goal': 'Meta Diaria'}
)

# Layout
layout = html.Div([
    html.H2("Análisis de Actividad Diaria"),
    html.Div(className="row", children=[
        html.Div(className="col", children=[dcc.Graph(figure=activity_calories)]),
        html.Div(className="col", children=[dcc.Graph(figure=activity_steps)]),
    ]),
    html.Div(className="row", children=[
        html.Div(className="col", children=[dcc.Graph(figure=activity_active_time)]),
        html.Div(className="col", children=[dcc.Graph(figure=activity_goal)]),
    ])
])
