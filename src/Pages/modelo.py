from dash import dcc, html, Input, Output, callback
import pandas as pd
import numpy as np
from Model.model_training import prepare_synthetic_data, train_simple_model

# Preparar datos y entrenar el modelo
X, y = prepare_synthetic_data()
model, scaler = train_simple_model(X, y)

# Layout
layout = html.Div(className="model-page", children=[
    html.H2("Modelo de Predicción con Datos Sintéticos"),
    html.Div(children=[
        html.Label("Puntaje de Estrés:"),
        dcc.Input(id="input-stress-score", type="number", placeholder="Ingresa el puntaje de estrés"),
        html.Label("Duración del Sueño (minutos):"),
        dcc.Input(id="input-sleep-duration", type="number", placeholder="Ingresa la duración del sueño"),
        html.Label("Eficiencia del Sueño (%):"),
        dcc.Input(id="input-efficiency", type="number", placeholder="Ingresa la eficiencia del sueño"),
        html.Label("Temperatura (°C):"),
        dcc.Input(id="input-temperature", type="number", placeholder="Ingresa la temperatura"),
        html.Label("Humedad (%):"),
        dcc.Input(id="input-humidity", type="number", placeholder="Ingresa la humedad"),
        html.Button("Predecir", id="predict-btn"),
        html.Div(id="prediction-output", style={"margin-top": "20px"})
    ])
])

# Callback
@callback(
    Output("prediction-output", "children"),
    Input("predict-btn", "n_clicks"),
    [
        Input("input-stress-score", "value"),
        Input("input-sleep-duration", "value"),
        Input("input-efficiency", "value"),
        Input("input-temperature", "value"),
        Input("input-humidity", "value")
    ]
)
def make_prediction(n_clicks, stress_score, sleep_duration, efficiency, temperature, humidity):
    if n_clicks is None or None in [stress_score, sleep_duration, efficiency, temperature, humidity]:
        return "Por favor, completa todos los campos."

    # Crear el input para el modelo
    input_data = pd.DataFrame(
        [[stress_score, sleep_duration, efficiency, temperature, humidity]], 
        columns=X.columns
    )
    input_data_scaled = scaler.transform(input_data)

    # Realizar la predicción
    prediction = model.predict(input_data_scaled)
    if prediction[0] == 1:
        return "Es probable que puedas realizar ejercicio."
    else:
        return "Es probable que no puedas realizar ejercicio."
