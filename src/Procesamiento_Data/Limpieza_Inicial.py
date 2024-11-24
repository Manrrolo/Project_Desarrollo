import os
import pandas as pd
import csv

# Rutas de entrada y salida
input_folder = './CSV'
output_folder = './Processed_CSV'
os.makedirs(output_folder, exist_ok=True)

def process_csv(file_path, output_folder):
    """
    Procesa un archivo CSV ajustando encabezados y columnas, y lo guarda en la carpeta de salida.
    """
    try:
        with open(file_path, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file, delimiter=',')
            rows = [row for row in reader]

        rows = rows[1:]  # Ignorar la primera línea
        headers = rows[0]  # Usar la segunda línea como encabezados
        max_columns = max(len(row) for row in rows[1:])  # Detectar número máximo de columnas

        if len(headers) < max_columns:
            headers += [f"Extra_Column_{i}" for i in range(len(headers), max_columns)]

        cleaned_df = pd.DataFrame(rows[1:], columns=headers[:max_columns])
        output_path = os.path.join(output_folder, f'cleaned_{os.path.basename(file_path)}')
        cleaned_df.to_csv(output_path, index=False)

        print(f"Archivo procesado: {output_path}")
    except Exception as e:
        print(f"Error procesando {file_path}: {e}")

# Procesar todos los archivos CSV en la carpeta de entrada
for file_name in os.listdir(input_folder):
    if file_name.endswith('.csv'):
        process_csv(os.path.join(input_folder, file_name), output_folder)

print(f"Archivos procesados y guardados en: {output_folder}")

# Nota para el usuario:
# Este script debe ejecutarse desde la carpeta `Procesamiento_Data`.
