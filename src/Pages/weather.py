from dash import dcc, html, Input, Output, callback
import plotly.express as px
from data_processing import load_and_clean_data

# Cargar y limpiar datos
data = load_and_clean_data(
    "./Data/filtered_cleaned_com.samsung.shealth.exercise.weather.20241124164179_processed.csv"
)

# Extraer DataFrame
weather_data = data["filtered_cleaned_com.samsung.shealth.exercise.weather.20241124164179_processed.csv"]

# Crear gráficos principales
weather_boxplot = px.box(
    weather_data,
    x='phrase',
    y='temperature',
    title='Distribución de Temperaturas por Tipo de Clima',
    labels={'phrase': 'Tipo de Clima', 'temperature': 'Temperatura (°C)'}
)

weather_histogram = px.histogram(
    weather_data,
    x='temperature',
    color='phrase',
    title='Distribución de Temperaturas',
    labels={'temperature': 'Temperatura (°C)', 'phrase': 'Tipo de Clima'}
)

weather_scatter = px.scatter(
    weather_data,
    x='wind_speed',
    y='humidity',
    color='phrase',
    title='Relación entre Velocidad del Viento y Humedad',
    labels={'wind_speed': 'Velocidad del Viento (m/s)', 'humidity': 'Humedad (%)', 'phrase': 'Tipo de Clima'}
)

# Gráfico con filtro
filtered_weather_graph = dcc.Graph(id='filtered-weather-graph')

# Layout para la página de Ejercicio y Clima
layout = html.Div([
    html.H2("Análisis de Ejercicio y Clima"),
    html.Div(className="row", children=[
        html.Div(className="col", children=[dcc.Graph(figure=weather_boxplot)]),
        html.Div(className="col", children=[dcc.Graph(figure=weather_histogram)]),
    ]),
    html.Div(className="row", children=[
        html.Div(className="col", children=[
            html.Label("Filtrar por rango de fechas:"),
            dcc.DatePickerRange(
                id='weather-date-filter',
                start_date=weather_data['timestamp'].min(),
                end_date=weather_data['timestamp'].max(),
                display_format="YYYY-MM-DD",
            ),
            html.Label("Filtrar por tipo de clima:"),
            dcc.Dropdown(
                id='weather-type-filter',
                options=[
                    {"label": str(climate), "value": climate} for climate in weather_data['phrase'].unique()
                ],
                multi=True,
                placeholder="Selecciona tipos de clima",
            ),
            filtered_weather_graph
        ]),
        html.Div(className="col", children=[
            dcc.Graph(figure=weather_scatter)
        ])
    ])
])

# Callback para el gráfico con filtro
@callback(
    Output('filtered-weather-graph', 'figure'),
    [Input('weather-date-filter', 'start_date'),
     Input('weather-date-filter', 'end_date'),
     Input('weather-type-filter', 'value')]
)
def update_filtered_weather_graph(start_date, end_date, selected_types):
    filtered_data = weather_data.copy()
    if start_date and end_date:
        filtered_data = filtered_data[
            (filtered_data['timestamp'] >= start_date) & 
            (filtered_data['timestamp'] <= end_date)
        ]
    if selected_types:
        filtered_data = filtered_data[filtered_data['phrase'].isin(selected_types)]

    fig = px.scatter(
        filtered_data,
        x='timestamp', y='temperature',
        color='phrase',
        title='Temperaturas Filtradas por Tipo de Clima',
        labels={'timestamp': 'Fecha', 'temperature': 'Temperatura (°C)', 'phrase': 'Tipo de Clima'}
    )
    return fig
