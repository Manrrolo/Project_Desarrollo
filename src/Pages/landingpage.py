from dash import html

layout = html.Div(className="landing-page", children=[
    html.Div(
        children=[
            html.H1("Bienvenido al Dashboard de Salud"),
            html.P(
                "Este proyecto utiliza datos de salud para analizar tendencias y realizar predicciones."
            )
        ]
    ),
    html.Div(className="landing-page-icons", children=[
        html.Div(children=[
            html.Img(src="https://cdn-icons-png.flaticon.com/512/2620/2620282.png"),
            html.H4("Análisis de Datos"),
            html.P("Gráficos detallados sobre tus datos de salud.")
        ]),
        html.Div(children=[
            html.Img(src="https://cdn-icons-png.flaticon.com/512/2936/2936635.png"),
            html.H4("Predicciones"),
            html.P("Usa modelos para predecir métricas clave.")
        ]),
        html.Div(children=[
            html.Img(src="https://cdn-icons-png.flaticon.com/512/3176/3176293.png"),
            html.H4("Sobre Nosotros"),
            html.P("Conoce más sobre el creador del proyecto.")
        ])
    ])
])
