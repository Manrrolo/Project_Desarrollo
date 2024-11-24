import os
import pandas as pd

# Rutas de las carpetas
processed_data_folder = './Processed_Data'
final_data_folder = './Final_Data'
summary_data_folder = './Summary_Data'

# Crear carpetas si no existen
os.makedirs(final_data_folder, exist_ok=True)
os.makedirs(summary_data_folder, exist_ok=True)

# Columnas relevantes por archivo (ordenados según tu numeración)
columns_mapping = {
    "cleaned_com.samsung.health.oxygen_saturation.raw": [
        "start_time", "update_time", "create_time", "is_integrated", "time_offset",
        "end_time", "time", "channel"
    ],
    "cleaned_com.samsung.shealth.activity.day_summary": [
        "exercise_time", "step_count", "exercise_calorie_target", "active_time", "target",
        "others_time", "update_time", "floors_target", "create_time", "floor_count",
        "dynamic_active_time_target", "exercise_time_target", "goal", "longest_active_time",
        "score", "move_hourly_count", "duration_type", "move_hourly_target", "distance",
        "dynamic_active_time", "calorie", "extra_data", "walk_time", "longest_idle_time",
        "datauuid", "day_time"
    ],
    "cleaned_com.samsung.shealth.exercise": [
        "heart_rate_sample_count", "start_latitude", "mission_extra_value", "program_schedule_id",
        "heart_rate_deviceuuid", "location_data_internal", "custom_id", "additional_internal",
        "com.samsung.health.exercise.duration", "com.samsung.health.exercise.additional",
        "com.samsung.health.exercise.create_sh_ver", "com.samsung.health.exercise.mean_caloricburn_rate",
        "com.samsung.health.exercise.location_data", "com.samsung.health.exercise.start_time",
        "com.samsung.health.exercise.exercise_type", "com.samsung.health.exercise.custom",
        "com.samsung.health.exercise.max_altitude", "com.samsung.health.exercise.incline_distance",
        "com.samsung.health.exercise.mean_heart_rate", "com.samsung.health.exercise.count_type",
        "com.samsung.health.exercise.mean_rpm", "com.samsung.health.exercise.min_altitude",
        "com.samsung.health.exercise.modify_sh_ver", "com.samsung.health.exercise.max_heart_rate",
        "com.samsung.health.exercise.update_time", "com.samsung.health.exercise.create_time",
        "com.samsung.health.exercise.max_power", "com.samsung.health.exercise.max_speed",
        "com.samsung.health.exercise.mean_cadence", "com.samsung.health.exercise.min_heart_rate",
        "com.samsung.health.exercise.count", "com.samsung.health.exercise.distance",
        "com.samsung.health.exercise.max_caloricburn_rate", "com.samsung.health.exercise.calorie",
        "com.samsung.health.exercise.max_cadence", "com.samsung.health.exercise.decline_distance",
        "com.samsung.health.exercise.vo2_max", "com.samsung.health.exercise.time_offset",
        "com.samsung.health.exercise.deviceuuid", "com.samsung.health.exercise.max_rpm",
        "com.samsung.health.exercise.comment", "com.samsung.health.exercise.live_data",
        "com.samsung.health.exercise.mean_power", "com.samsung.health.exercise.mean_speed",
        "com.samsung.health.exercise.pkg_name", "com.samsung.health.exercise.altitude_gain",
        "com.samsung.health.exercise.altitude_loss", "com.samsung.health.exercise.exercise_custom_type",
        "com.samsung.health.exercise.auxiliary_devices", "com.samsung.health.exercise.end_time",
        "com.samsung.health.exercise.datauuid", "com.samsung.health.exercise.sweat_loss"
    ],
    "cleaned_com.samsung.shealth.exercise.recovery_heart_rate": [
        "start_time", "modify_sh_ver", "update_time", "create_time", "time_offset",
        "end_time", "datauuid", "heart_rate"
    ],
    "cleaned_com.samsung.shealth.exercise.weather": [
        "sunset_time", "start_time", "latitude", "custom", "wind_direction", "phrase",
        "sundown_time", "temperature_scale", "content_provider", "update_time",
        "create_time", "type", "longitude", "temperature", "humidity", "time_offset",
        "wind_speed_unit", "forecast_time", "wind_speed"
    ],
    "cleaned_com.samsung.shealth.sleep_combined": [
        "start_time", "mental_recovery", "factor_01", "factor_02", "factor_03", "factor_04",
        "factor_05", "factor_06", "factor_07", "factor_08", "factor_09", "factor_10",
        "has_sleep_data", "total_rem_duration", "modify_sh_ver", "update_time",
        "create_time", "sleep_type", "data_version", "physical_recovery", "original_wake_up_time",
        "movement_awakening", "original_bed_time", "goal_bed_time", "quality", "time_offset",
        "extra_data", "deviceuuid", "goal_wake_up_time", "sleep_cycle", "total_light_duration",
        "efficiency", "sleep_score", "pkg_name", "sleep_duration", "stage_analyzed_type",
        "end_time", "datauuid", "stage_analysis_type"
    ],
    "cleaned_com.samsung.shealth.step_daily_trend": [
        "update_time", "create_time", "source_pkg_name", "source_type", "count",
        "speed", "distance", "calorie", "day_time"
    ],
    "cleaned_com.samsung.shealth.stress": [
        "start_time", "custom", "update_time", "create_time", "max", "min", "score",
        "algorithm", "time_offset", "end_time", "score_max", "score_min", "flag", "level"
    ],
    "cleaned_com.samsung.shealth.tracker.pedometer_day_summary": [
        "step_count", "active_time", "recommendation", "run_step_count", "update_time",
        "source_package_name", "create_time", "source_info", "speed", "distance", "calorie",
        "walk_step_count", "healthy_step", "achievement", "day_time"
    ],
    "cleaned_com.samsung.shealth.tracker.pedometer_step_count": [
        "duration", "run_step", "walk_step", "com.samsung.health.step_count.start_time",
        "com.samsung.health.step_count.sample_position_type", "com.samsung.health.step_count.custom",
        "com.samsung.health.step_count.update_time", "com.samsung.health.step_count.create_time",
        "com.samsung.health.step_count.count", "com.samsung.health.step_count.speed",
        "com.samsung.health.step_count.distance", "com.samsung.health.step_count.calorie",
        "com.samsung.health.step_count.time_offset", "com.samsung.health.step_count.deviceuuid",
        "com.samsung.health.step_count.pkg_name", "com.samsung.health.step_count.end_time",
        "com.samsung.health.step_count.datauuid"
    ]
}

# Filtrar columnas y generar resumen
for file_name in os.listdir(processed_data_folder):
    print(f"Procesando: {file_name}")
    if file_name.endswith('_processed.csv'):
        file_key = file_name.split('_processed.csv')[0].rsplit('.', 1)[0]  # Remover el número y punto final
        print(f"Archivo clave: {file_key}")
        file_path = os.path.join(processed_data_folder, file_name)

        if file_key in columns_mapping:
            columns_to_keep = columns_mapping[file_key]
            data = pd.read_csv(file_path)
            filtered_data = data[columns_to_keep]
            
            # Guardar datos filtrados
            final_file_path = os.path.join(final_data_folder, f'filtered_{file_name}')
            filtered_data.to_csv(final_file_path, index=False)
            
            # Crear y guardar resumen
            summary = filtered_data.describe(include='all').transpose()
            summary_file_path = os.path.join(summary_data_folder, f'summary_{file_name}')
            summary.to_csv(summary_file_path)
            
            print(f"Procesado: {file_name}")



