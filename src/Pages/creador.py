from dash import html

layout = html.Div(className="about-page", children=[
    html.Div(children=[
        html.H2("Sobre el Creador"),
        html.P("Conoce más sobre el autor de este proyecto.")
    ]),
    html.Div(children=[
        html.Img(src="https://raw.githubusercontent.com/Manrrolo/Page/refs/heads/main/20240709_145510%20(1).jpg"),
        html.H4("Manuel Sepúlveda"),
        html.P(
            className="description",
            children=(
                "Soy un desarrollador de software apasionado por el análisis de datos, "
                "la visualización y el aprendizaje automático. Disfruto resolver problemas "
                "y crear soluciones digitales que generen impacto positivo. "
            )
        ),
    ])
])
