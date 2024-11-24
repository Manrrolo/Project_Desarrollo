from dash import dcc, html

layout = html.Div(className="model-page", children=[
    html.Div(children=[
        html.H2("Modelo de Machine Learning"),
        html.P("Realiza predicciones basadas en los datos ingresados."),
        html.Img(src="https://plus.unsplash.com/premium_photo-1720287601300-cf423c3d6760")
    ]),
    html.Div(children=[
        dcc.Input(id='input-data', type='number', placeholder="Ingresa un valor"),
        html.Button("Predecir", id='predict-btn'),
        html.Div(id='prediction-output')
    ])
])
