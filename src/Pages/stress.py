from dash import dcc, html, Input, Output, callback
import plotly.express as px
from data_processing import load_and_clean_data

# Cargar y limpiar datos
data = load_and_clean_data(
    "./Data/filtered_cleaned_com.samsung.shealth.stress.20241124164179_processed.csv"
)

# Extraer DataFrame
stress_data = data["filtered_cleaned_com.samsung.shealth.stress.20241124164179_processed.csv"]

# Crear gráficos principales
stress_boxplot = px.box(
    stress_data,
    x='level',
    y='stress_score',
    title='Distribución de Puntajes de Estrés por Nivel',
    labels={'level': 'Nivel de Estrés', 'stress_score': 'Puntaje de Estrés'}
)

stress_scatter = px.scatter(
    stress_data,
    x='stress_score',
    y='level',
    title='Relación entre Puntaje de Estrés y Nivel',
    labels={'stress_score': 'Puntaje de Estrés', 'level': 'Nivel de Estrés'}
)

stress_histogram = px.histogram(
    stress_data,
    x='stress_score',
    color='level',
    barmode='overlay',
    title='Distribución de Puntajes de Estrés',
    labels={'stress_score': 'Puntaje de Estrés', 'level': 'Nivel de Estrés'}
)

# Layout para la página de Estrés
layout = html.Div([
    html.H2("Análisis de Estrés"),
    html.Div(className="row", children=[
        html.Div(className="col", children=[dcc.Graph(figure=stress_boxplot)]),
        html.Div(className="col", children=[dcc.Graph(figure=stress_scatter)]),
    ]),
    html.Div(className="row", children=[
        html.Div(className="col", children=[dcc.Graph(figure=stress_histogram)]),
        html.Div(className="col", children=[
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
            ),
            dcc.Graph(id='filtered-stress-graph')
        ])
    ])
])

# Callback para el gráfico con filtro
@callback(
    Output('filtered-stress-graph', 'figure'),
    [Input('stress-date-filter', 'start_date'),
     Input('stress-date-filter', 'end_date'),
     Input('stress-level-filter', 'value')]
)
def update_filtered_stress_graph(start_date, end_date, selected_levels):
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
