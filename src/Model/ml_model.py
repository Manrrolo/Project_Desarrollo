from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

def train_model(data, target_column):
    X = data.drop(columns=[target_column])
    y = data[target_column]

    # Dividir en conjunto de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Entrenar un modelo de Random Forest
    model = RandomForestRegressor(random_state=42)
    model.fit(X_train, y_train)

    # Evaluación básica
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)

    return model, mse

def predict(model, input_data):
    return model.predict(input_data)
