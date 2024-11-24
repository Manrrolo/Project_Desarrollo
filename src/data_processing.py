import pandas as pd

def load_and_clean_data(step_path, stress_combined_path, pedometer_path):
    # Cargar los datos
    step_daily = pd.read_csv(step_path)
    stress_combined = pd.read_csv(stress_combined_path)
    tracker_pedometer = pd.read_csv(pedometer_path)

    # Limpieza de Step Daily
    step_daily_clean = step_daily[['source_type', 'count', 'speed', 'distance', 'calorie', 'day_time']]
    step_daily_clean.rename(columns={
        'count': 'step_count',
        'calorie': 'calories',
        'day_time': 'timestamp'
    }, inplace=True)
    step_daily_clean['timestamp'] = pd.to_datetime(step_daily_clean['timestamp'], unit='ms')

    # Limpieza de Stress Combined
    stress_combined_clean = stress_combined[['start_time', 'max', 'min', 'score', 'score_max', 'score_min', 'level']]
    stress_combined_clean['start_time'] = pd.to_datetime(stress_combined_clean['start_time'], unit='ms')

    # Limpieza de Tracker Pedometer
    tracker_pedometer_clean = tracker_pedometer[['step_count', 'active_time', 'distance', 'calorie', 'speed']]
    tracker_pedometer_clean.rename(columns={
        'active_time': 'active_time_seconds',
        'distance': 'distance_km',
        'calorie': 'calories',
        'speed': 'avg_speed_kmh',
    }, inplace=True)

    return step_daily_clean, stress_combined_clean, tracker_pedometer_clean
