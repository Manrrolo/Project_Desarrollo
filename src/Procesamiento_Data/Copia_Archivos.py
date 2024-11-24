import os
import shutil

# Rutas de las carpetas
current_folder = os.getcwd()  # Carpeta actual
final_data_folder = os.path.join(current_folder, 'Final_Data')
summary_data_folder = os.path.join(current_folder, 'Summary_Data')
parent_data_folder = os.path.abspath(os.path.join(current_folder, '../Data'))

# Crear la carpeta 'Data' si no existe
os.makedirs(parent_data_folder, exist_ok=True)

# Función para copiar archivos
def copy_files_to_data(source_folder, target_folder):
    for file_name in os.listdir(source_folder):
        source_path = os.path.join(source_folder, file_name)
        target_path = os.path.join(target_folder, file_name)
        if os.path.isfile(source_path):
            shutil.copy2(source_path, target_path)
            print(f"Archivo copiado: {file_name} a {target_folder}")

# Copiar archivos de Final_Data y Summary_Data a la carpeta Data
print("Copiando archivos de Final_Data...")
copy_files_to_data(final_data_folder, parent_data_folder)

print("Copiando archivos de Summary_Data...")
copy_files_to_data(summary_data_folder, parent_data_folder)

print(f"Todos los archivos han sido copiados a la carpeta: {parent_data_folder}")
