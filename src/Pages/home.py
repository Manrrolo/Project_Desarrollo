from dash import dcc, html
import plotly.express as px
from data_processing import load_and_clean_data

# Cargar y limpiar datos
step_data, stress_data, pedometer_data = load_and_clean_data(
    "./Data/step_daily_trend_numeric_summary.csv",
    "./Data/filtered_cleaned_com.samsung.shealth.stress.20241124164179_processed.csv",
    "./Data/tracker_pedometer_numeric_summary.csv"
)

# Layout de la página
layout = html.Div(className="home-page", children=[
    html.Div(children=[
        html.H2("Dashboard Principal"),
        html.P("Explora los datos de salud recopilados a continuación.")
    ]),
    html.Div(className="graph-section", children=[
        html.H4("Pasos Diarios"),
        html.Img(src="https://images.unsplash.com/photo-1690016424217-03f4d9427a6a"),
        dcc.Graph(
            id='steps-graph',
            figure=px.line(step_data, x='timestamp', y='step_count', title='Pasos Diarios')
        )
    ]),
    html.Div(className="graph-section", children=[
        html.H4("Niveles de Estrés"),
        html.Img(src="https://images.unsplash.com/photo-1456406644174-8ddd4cd52a06"),
        dcc.Graph(
            id='stress-graph',
            figure=px.line(stress_data, x='start_time', y='score', title='Niveles de Estrés')
        )
    ]),
    html.Div(className="graph-section", children=[
        html.H4("Calorías Quemadas"),
        html.Img(src="https://images.unsplash.com/photo-1605296867304-46d5465a13f1"),
        dcc.Graph(
            id='pedometer-graph',
            figure=px.line(pedometer_data, x=pedometer_data.index, y='calories', title='Calorías Quemadas')
        )
    ])
])
