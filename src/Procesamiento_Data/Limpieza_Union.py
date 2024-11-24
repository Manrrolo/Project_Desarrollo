import os
import json
import pandas as pd
import shutil

# Rutas de las carpetas
csv_folder = './Processed_CSV'
json_base_folder = './jsons'
output_folder = './Output'
os.makedirs(output_folder, exist_ok=True)

def process_csv_with_json(file_name):
    """
    Procesa un archivo CSV combinando filas con los JSON relacionados y guarda los resultados.
    """
    try:
        csv_path = os.path.join(csv_folder, file_name)
        csv_data = pd.read_csv(csv_path)

        # Verificar si hay columnas que contienen identificadores de JSON, como 'binning_data' o 'Heart_rate'
        relevant_columns = [col for col in ['binning_data', 'Heart_rate'] if col in csv_data.columns]
        if not relevant_columns:
            print(f"El archivo {file_name} no contiene columnas relevantes para procesar JSON.")
            csv_data.to_csv(os.path.join(output_folder, file_name), index=False)
            return

        processed_data = []
        for _, row in csv_data.iterrows():
            combined_data = row.to_dict()
            for col in relevant_columns:
                json_key = row[col]
                if pd.isna(json_key):
                    continue
                first_char = json_key[0]
                json_file_path = os.path.join(json_base_folder, file_name.split('cleaned_')[1].rsplit('.', 2)[0], first_char, f'{json_key}')

                if os.path.exists(json_file_path) and os.path.getsize(json_file_path) > 0:
                    with open(json_file_path, 'r') as json_file:
                        try:
                            json_data = json.load(json_file)

                            # Verificar si json_data es iterable (lista o diccionario)
                            if isinstance(json_data, list):
                                for record in json_data:
                                    temp_data = combined_data.copy()
                                    temp_data.update(record)
                                    processed_data.append(temp_data)
                            elif isinstance(json_data, dict):
                                combined_data.update(json_data)
                                processed_data.append(combined_data)
                            else:
                                print(f"Advertencia: JSON en {json_file_path} no es iterable.")
                        except json.JSONDecodeError:
                            print(f"Error decodificando JSON en {json_file_path}.")
                else:
                    print(f"Archivo JSON no encontrado o vacío para {json_key}.")
                    processed_data.append(combined_data)

        # Guardar los datos procesados
        output_file_name = file_name.replace('.csv', '_processed.csv')
        output_path = os.path.join(output_folder, output_file_name)
        pd.DataFrame(processed_data).to_csv(output_path, index=False)
        print(f"Procesado y guardado en: {output_path}")

    except Exception as e:
        print(f"Error procesando {file_name}: {e}")
        csv_data.to_csv(os.path.join(output_folder, file_name), index=False)

# Procesar todos los archivos CSV en la carpeta
for file_name in os.listdir(csv_folder):
    if file_name.endswith('.csv'):
        process_csv_with_json(file_name)

# Nota final
print(f"Todos los archivos han sido procesados y guardados en: {output_folder}")

# Carpeta de salida y carpeta de datos procesados
output_folder = './Output'
processed_data_folder = './Processed_Data'
os.makedirs(processed_data_folder, exist_ok=True)

# Lista de archivos que deben ser movidos
files_to_move = [
    "cleaned_com.samsung.health.oxygen_saturation.raw.20241124164179_processed.csv",
    "cleaned_com.samsung.shealth.activity.day_summary.20241124164179_processed.csv",
    "cleaned_com.samsung.shealth.exercise.20241124164179_processed.csv",
    "cleaned_com.samsung.shealth.exercise.recovery_heart_rate.20241124164179_processed.csv",
    "cleaned_com.samsung.shealth.exercise.weather.20241124164179_processed.csv",
    "cleaned_com.samsung.shealth.sleep_combined.20241124164179_processed.csv",
    "cleaned_com.samsung.shealth.step_daily_trend.20241124164179_processed.csv",
    "cleaned_com.samsung.shealth.stress.20241124164179_processed.csv",
    "cleaned_com.samsung.shealth.tracker.pedometer_day_summary.20241124164179_processed.csv",
    "cleaned_com.samsung.shealth.tracker.pedometer_step_count.20241124164179_processed.csv",
]

# Mover archivos a la carpeta de datos procesados
for file_name in files_to_move:
    source_path = os.path.join(output_folder, file_name)
    destination_path = os.path.join(processed_data_folder, file_name)

    if os.path.exists(source_path):
        shutil.move(source_path, destination_path)
        print(f"Archivo movido: {file_name}")
    else:
        print(f"Archivo no encontrado en {output_folder}: {file_name}")

# Nota final
print(f"Todos los archivos especificados se han movido a la carpeta: {processed_data_folder}")
