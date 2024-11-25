import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

def generate_synthetic_data(start_date, end_date, num_samples, column_ranges):
    """
    Genera datos sintéticos para un rango de fechas y columnas dadas.
    """
    dates = pd.date_range(start=start_date, end=end_date, periods=num_samples)
    synthetic_data = {"timestamp": dates}
    
    for column, (low, high) in column_ranges.items():
        synthetic_data[column] = np.random.uniform(low, high, num_samples)
    
    return pd.DataFrame(synthetic_data)

def prepare_synthetic_data():
    """
    Genera datos sintéticos para estrés, clima y sueño en el mismo rango de fechas.
    """
    # Definir el rango de fechas y el número de muestras
    start_date = "2023-01-01"
    end_date = "2024-12-31"
    num_samples = 1000  # Número de registros simulados
    
    # Definir rangos de valores para cada columna
    stress_ranges = {"stress_score": (10, 100)}
    sleep_ranges = {"sleep_duration": (300, 600), "efficiency": (50, 100)}
    weather_ranges = {"temperature": (10, 35), "humidity": (30, 90)}
    
    # Generar datos sintéticos
    stress_data = generate_synthetic_data(start_date, end_date, num_samples, stress_ranges)
    sleep_data = generate_synthetic_data(start_date, end_date, num_samples, sleep_ranges)
    weather_data = generate_synthetic_data(start_date, end_date, num_samples, weather_ranges)
    
    # Merge de los datasets en base a la columna "timestamp"
    merged_data = pd.merge(stress_data, sleep_data, on="timestamp", how="inner")
    merged_data = pd.merge(merged_data, weather_data, on="timestamp", how="inner")
    
    # Crear la etiqueta de predicción
    merged_data["can_exercise"] = np.where(
        (
            (merged_data["stress_score"] < 50) |  # Estrés bajo O
            ((merged_data["stress_score"] >= 50) &  # Estrés alto pero...
             (merged_data["sleep_duration"] > 360) &  # Durmió más de 6 horas
             (merged_data["efficiency"] > 75) &  # Eficiencia del sueño > 75%
             (merged_data["temperature"].between(10, 30)) &  # Temperatura cómoda
             (merged_data["humidity"] < 80))  # Humedad moderada
        ),
        1,  # Puede realizar ejercicio
        0   # No puede realizar ejercicio
    )
    
    # Dividir en X (entrada) e y (etiqueta)
    X = merged_data.drop(columns=["can_exercise", "timestamp"])
    y = merged_data["can_exercise"]
    
    return X, y

def train_simple_model(X, y):
    """
    Entrenar un modelo simple con los datos generados.
    """
    # Escalar los datos
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Dividir los datos en entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

    # Entrenar un modelo simple (Random Forest)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    return model, scaler
