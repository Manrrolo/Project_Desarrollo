from dash import dcc, html, Input, Output, callback
import plotly.express as px
from data_processing import load_and_clean_data

# Cargar y limpiar datos
data = load_and_clean_data(
    "./Data/filtered_cleaned_com.samsung.shealth.stress.20241124164179_processed.csv",
    "./Data/filtered_cleaned_com.samsung.shealth.sleep_combined.20241124164179_processed.csv",
    "./Data/filtered_cleaned_com.samsung.health.oxygen_saturation.raw.20241124164179_processed.csv"
)

# Extraer DataFrames
stress_data = data["filtered_cleaned_com.samsung.shealth.stress.20241124164179_processed.csv"]
sleep_data = data["filtered_cleaned_com.samsung.shealth.sleep_combined.20241124164179_processed.csv"]
oxygen_data = data["filtered_cleaned_com.samsung.health.oxygen_saturation.raw.20241124164179_processed.csv"]

# Crear gráficos principales
stress_histogram = px.histogram(
    stress_data,
    x='stress_score',
    color='level',
    barmode='overlay',
    title='Distribución de Puntajes de Estrés',
    labels={'stress_score': 'Puntaje de Estrés', 'level': 'Nivel de Estrés'}
)

sleep_scatter = px.scatter(
    sleep_data,
    x='timestamp',
    y='sleep_duration',
    title='Duración de Sueño en el Tiempo',
    labels={'timestamp': 'Fecha', 'sleep_duration': 'Duración de Sueño (minutos)'}
)

oxygen_histogram = px.histogram(
    oxygen_data,
    x='time',
    title='Distribución del Tiempo de Saturación de Oxígeno',
    labels={'time': 'Tiempo (s)'}
)

# Layout para la página principal
layout = html.Div(className="home-page", children=[
    html.H2("Dashboard Principal"),
    html.P("Explora los datos principales de Estrés, Sueño y Oxígeno Saturación."),
    html.Div(className="row", children=[
        html.Div(className="col", children=[dcc.Graph(figure=stress_histogram)]),
        html.Div(className="col", children=[
            html.Label("Filtrar por rango de fechas:"),
            dcc.DatePickerRange(
                id='stress-date-filter-home',
                start_date=stress_data['timestamp'].min(),
                end_date=stress_data['timestamp'].max(),
                display_format="YYYY-MM-DD",
            ),
            html.Label("Filtrar por nivel de estrés:"),
            dcc.Dropdown(
                id='stress-level-filter-home',
                options=[
                    {"label": str(level), "value": level} for level in stress_data['level'].unique()
                ],
                multi=True,
                placeholder="Selecciona niveles de estrés",
            ),
            dcc.Graph(id='filtered-stress-graph-home')
        ]),
    ]),
    html.Div(className="row", children=[
        html.Div(className="col", children=[dcc.Graph(figure=oxygen_histogram)]),
        html.Div(className="col", children=[dcc.Graph(figure=sleep_scatter)]),
    ]),
])

# Callback para el gráfico con filtro
@callback(
    Output('filtered-stress-graph-home', 'figure'),
    [Input('stress-date-filter-home', 'start_date'),
     Input('stress-date-filter-home', 'end_date'),
     Input('stress-level-filter-home', 'value')]
)
def update_filtered_stress_graph_home(start_date, end_date, selected_levels):
    filtered_data = stress_data.copy()
    if start_date and end_date:
        filtered_data = filtered_data[
            (filtered_data['timestamp'] >= start_date) & 
            (filtered_data['timestamp'] <= end_date)
        ]
    if selected_levels:
        filtered_data = filtered_data[filtered_data['level'].isin(selected_levels)]

    fig = px.scatter(
        filtered_data,
        x='timestamp', y='stress_score',
        color='level',
        title='Niveles de Estrés Filtrados',
        labels={'timestamp': 'Fecha', 'stress_score': 'Puntaje de Estrés', 'level': 'Nivel de Estrés'}
    )
    return fig
