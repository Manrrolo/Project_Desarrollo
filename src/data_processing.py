import pandas as pd


def load_and_clean_data(*file_paths):
    """
    Carga y limpia los datos de múltiples archivos CSV.

    Args:
        file_paths: Rutas de los archivos a cargar.

    Returns:
        dict: Diccionario con nombres de archivo como claves y DataFrames limpios como valores.
    """
    datasets = {}

    for file_path in file_paths:
        file_name = file_path.split("/")[-1]
        if "stress_combined" in file_name or "pedometer_day_summary" in file_name:
            # Excluir los archivos especificados
            print(f"Excluyendo archivo: {file_name}")
            continue

        df = pd.read_csv(file_path)

        try:
            if "numeric_summary" in file_name or "summary_cleaned" in file_name:
                # Limpieza para archivos de tipo resumen
                stats_columns = ['mean', 'std', 'min', 'max']
                df_clean = df[[col for col in df.columns if col in stats_columns]]
            
            elif "step_daily_trend" in file_name:
                # Limpieza de Step Daily
                df_clean = df[[ 'count', 'speed', 'distance', 'calorie', 'create_time']]
                df_clean.rename(columns={
                    'count': 'step_count',
                    'calorie': 'calories',
                    'create_time': 'timestamp'
                }, inplace=True)
                df_clean['timestamp'] = pd.to_datetime(df_clean['timestamp'], errors='coerce')


            elif "stress" in file_name:
                # Limpieza de Stress
                df_clean = df[['update_time', 'max', 'min', 'score', 'score_max', 'score_min', 'level']]
                df_clean.rename(columns={
                    'update_time': 'timestamp',
                    'score': 'stress_score'
                }, inplace=True)
                df_clean['timestamp'] = pd.to_datetime(df_clean['timestamp'], errors='coerce')

            elif "sleep_combined" in file_name:
                # Limpieza de Sleep Combined
                df_clean = df[['start_time', 'sleep_duration', 'sleep_score', 'efficiency']]
                df_clean.rename(columns={
                    'start_time': 'timestamp'
                }, inplace=True)
                df_clean['timestamp'] = pd.to_datetime(df_clean['timestamp'], errors='coerce')

            elif "oxygen_saturation" in file_name:
                # Limpieza de Oxygen Saturation
                df_clean = df[['start_time', 'end_time', 'channel', 'time']]
                df_clean.rename(columns={
                    'start_time': 'timestamp'
                }, inplace=True)
                df_clean['timestamp'] = pd.to_datetime(df_clean['timestamp'], errors='coerce')

            elif "weather" in file_name:
                # Limpieza de Weather
                df_clean = df[['start_time', 'temperature', 'humidity', 'wind_speed', 'phrase']]
                df_clean.rename(columns={
                    'start_time': 'timestamp'
                }, inplace=True)
                df_clean['timestamp'] = pd.to_datetime(df_clean['timestamp'], errors='coerce')

            elif "exercise" in file_name and "recovery" not in file_name:
                # Limpieza de Exercise
                df_clean = df[['com.samsung.health.exercise.start_time', 'com.samsung.health.exercise.calorie',
                               'com.samsung.health.exercise.distance', 'com.samsung.health.exercise.mean_speed']]
                df_clean.rename(columns={
                    'com.samsung.health.exercise.start_time': 'timestamp',
                    'com.samsung.health.exercise.calorie': 'calories'
                }, inplace=True)
                df_clean['timestamp'] = pd.to_datetime(df_clean['timestamp'], errors='coerce')

            elif "recovery_heart_rate" in file_name:
                # Limpieza de Recovery Heart Rate
                df_clean = df[['start_time', 'heart_rate']]
                df_clean.rename(columns={
                    'start_time': 'timestamp'
                }, inplace=True)
                df_clean['timestamp'] = pd.to_datetime(df_clean['timestamp'], errors='coerce')

            elif "activity.day_summary" in file_name:
                # Limpieza de Activity Day Summary
                df_clean = df[['exercise_time', 'step_count', 'active_time', 'calorie', 'goal', 'distance', 'create_time']]
                df_clean.rename(columns={
                    'create_time': 'timestamp',
                    'calorie': 'calories'
                }, inplace=True)
                df_clean['timestamp'] = pd.to_datetime(df_clean['timestamp'], errors='coerce')
                
            

            else:
                print(f"No se reconoció el archivo {file_name}, omitiendo procesamiento.")
                continue

            datasets[file_name] = df_clean

        except KeyError as e:
            print(f"Error procesando {file_name}: Columnas faltantes: {e}")
            continue

    return datasets
