from dash import dcc, html, Input, Output, callback
import plotly.express as px
from data_processing import load_and_clean_data

# Cargar y limpiar datos
data = load_and_clean_data(
    "./Data/step_daily_trend_numeric_summary.csv",
    "./Data/filtered_cleaned_com.samsung.shealth.stress.20241124164179_processed.csv",
    "./Data/filtered_cleaned_com.samsung.shealth.sleep_combined.20241124164179_processed.csv",
    "./Data/filtered_cleaned_com.samsung.health.oxygen_saturation.raw.20241124164179_processed.csv",
    "./Data/filtered_cleaned_com.samsung.shealth.activity.day_summary.20241124164179_processed.csv",
    "./Data/filtered_cleaned_com.samsung.shealth.exercise.20241124164179_processed.csv",
    "./Data/filtered_cleaned_com.samsung.shealth.exercise.recovery_heart_rate.20241124164179_processed.csv",
    "./Data/filtered_cleaned_com.samsung.shealth.exercise.weather.20241124164179_processed.csv",
    "./Data/filtered_cleaned_com.samsung.shealth.tracker.pedometer_step_count.20241124164179_processed.csv",
    "./Data/step_daily_trend_numeric_summary.csv",
    "./Data/stress_numeric_summary.csv",
    "./Data/summary_cleaned_com.samsung.health.oxygen_saturation.raw.20241124164179_processed.csv",
    "./Data/summary_cleaned_com.samsung.shealth.activity.day_summary.20241124164179_processed.csv",
    "./Data/summary_cleaned_com.samsung.shealth.exercise.20241124164179_processed.csv",
    "./Data/summary_cleaned_com.samsung.shealth.exercise.recovery_heart_rate.20241124164179_processed.csv",
    "./Data/summary_cleaned_com.samsung.shealth.exercise.weather.20241124164179_processed.csv",
    "./Data/summary_cleaned_com.samsung.shealth.sleep_combined.20241124164179_processed.csv",
    "./Data/summary_cleaned_com.samsung.shealth.step_daily_trend.20241124164179_processed.csv",
    "./Data/summary_cleaned_com.samsung.shealth.stress.20241124164179_processed.csv",
    "./Data/summary_cleaned_com.samsung.shealth.tracker.pedometer_step_count.20241124164179_processed.csv",
    "./Data/tracker_pedometer_numeric_summary.csv"
)

# Extraer DataFrames
stress_data = data["filtered_cleaned_com.samsung.shealth.stress.20241124164179_processed.csv"]
sleep_data = data["filtered_cleaned_com.samsung.shealth.sleep_combined.20241124164179_processed.csv"]
oxygen_data = data["filtered_cleaned_com.samsung.health.oxygen_saturation.raw.20241124164179_processed.csv"]

# Gráficos para el dataset de Estrés
stress_boxplot = px.box(
    stress_data,
    x='level',
    y='stress_score',
    title='Distribución de Puntajes de Estrés por Nivel',
    labels={'level': 'Nivel de Estrés (0: Bajo, 1: Alto)', 'stress_score': 'Puntaje de Estrés'}
)

stress_scatter = px.scatter(
    stress_data,
    x='stress_score',
    y='level',
    title='Relación entre Puntaje de Estrés y Nivel',
    labels={'stress_score': 'Puntaje de Estrés', 'level': 'Nivel de Estrés (0 o 1)'},
    opacity=0.5
)

stress_histogram = px.histogram(
    stress_data,
    x='stress_score',
    color='level',
    barmode='overlay',
    title='Distribución de Puntajes de Estrés',
    labels={'stress_score': 'Puntaje de Estrés', 'level': 'Nivel de Estrés (0: Bajo, 1: Alto)'}
)

# Filtros y gráfico dinámico para Estrés
filtered_stress_graph = dcc.Graph(id='filtered-stress-graph')
filters_section = html.Div([
    html.Label("Filtrar por rango de fechas:"),
    dcc.DatePickerRange(
        id='stress-date-filter',
        start_date=stress_data['timestamp'].min(),
        end_date=stress_data['timestamp'].max(),
        display_format="YYYY-MM-DD",
    ),
    html.Label("Filtrar por nivel de estrés:"),
    dcc.Dropdown(
        id='stress-level-filter',
        options=[
            {"label": str(level), "value": level} for level in stress_data['level'].unique()
        ],
        multi=True,
        placeholder="Selecciona niveles de estrés",
    )
])

# Gráficos para el dataset de Sueño
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

sleep_filtered = px.scatter(
    sleep_data,
    x='sleep_duration',
    y='efficiency',
    title='Relación entre Duración de Sueño y Eficiencia',
    labels={'sleep_duration': 'Duración de Sueño (minutos)', 'efficiency': 'Eficiencia'}
)

# Gráficos para el dataset de Oxígeno
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

oxygen_filtered = px.line(
    oxygen_data,
    x='timestamp',
    y='time',
    color='channel',
    title='Tendencia de Tiempo de Oxígeno por Canal',
    labels={'timestamp': 'Fecha', 'time': 'Tiempo (s)', 'channel': 'Canal'}
)

# Layout del dashboard
layout = html.Div(className="home-page", children=[
    html.Div(children=[
        html.H2("Dashboard Principal"),
        html.P("Explora los datos de salud recopilados a continuación."),
    ]),
    html.Div(children=[
        html.H3("Estrés"),
        html.Div(className="row", children=[
            html.Div(className="col", children=[dcc.Graph(figure=stress_boxplot)]),
            html.Div(className="col", children=[dcc.Graph(figure=stress_scatter)])
        ]),
        html.Div(className="row", children=[
            html.Div(className="col", children=[dcc.Graph(figure=stress_histogram)]),
            html.Div(className="col", children=[filters_section, filtered_stress_graph])
        ]),
    ]),
    html.Div(children=[
        html.H3("Sueño"),
        html.Div(className="row", children=[
            html.Div(className="col", children=[dcc.Graph(figure=sleep_boxplot)]),
            html.Div(className="col", children=[dcc.Graph(figure=sleep_scatter)])
        ]),
        html.Div(className="row", children=[
            html.Div(className="col", children=[dcc.Graph(figure=sleep_histogram)]),
            html.Div(className="col", children=[dcc.Graph(figure=sleep_filtered)])
        ]),
    ]),
    html.Div(children=[
        html.H3("Oxígeno Saturación"),
        html.Div(className="row", children=[
            html.Div(className="col", children=[dcc.Graph(figure=oxygen_boxplot)]),
            html.Div(className="col", children=[dcc.Graph(figure=oxygen_scatter)])
        ]),
        html.Div(className="row", children=[
            html.Div(className="col", children=[dcc.Graph(figure=oxygen_histogram)]),
            html.Div(className="col", children=[dcc.Graph(figure=oxygen_filtered)])
        ]),
    ])
])

# Callback para actualizar el gráfico de estrés filtrado
@callback(
    Output('filtered-stress-graph', 'figure'),
    [Input('stress-date-filter', 'start_date'),
     Input('stress-date-filter', 'end_date'),
     Input('stress-level-filter', 'value')]
)
def update_filtered_stress_graph(start_date, end_date, selected_levels):
    filtered_data = stress_data.copy()
    # Filtrar por rango de fechas
    if start_date and end_date:
        filtered_data = filtered_data[
            (filtered_data['timestamp'] >= start_date) &
            (filtered_data['timestamp'] <= end_date)
        ]
    # Filtrar por nivel de estrés
    if selected_levels:
        filtered_data = filtered_data[filtered_data['level'].isin(selected_levels)]

    # Crear gráfico filtrado
    fig = px.scatter(
        filtered_data,
        x='timestamp', y='stress_score',
        color='level',
        title='Niveles de Estrés Filtrados',
        labels={'timestamp': 'Fecha', 'stress_score': 'Puntaje de Estrés', 'level': 'Nivel de Estrés'}
    )
    return fig
