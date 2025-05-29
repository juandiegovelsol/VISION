import plotly.graph_objects as go

# Definir las categorías
categorias = ['SLG', 'OBP', 'BA', 'BB%', 'SO%', 'HR%', 'OPS']

# Definir datos para cada grupo
datos = {
    'Promedio MLB': {
        'valores': [0.410, 0.315, 0.245, 0.085, 0.230, 0.035, 0.725],
        'color': 'mediumpurple'
    },
    'Promedio BD': {
        'valores': [0.430, 0.325, 0.250, 0.090, 0.240, 0.040, 0.755],
        'color': 'tomato'
    },
    'Shohei Ohtani': {
        'valores': [0.592, 0.372, 0.257, 0.150, 0.295, 0.072, 0.965],
        'color': 'mediumseagreen'
    },
    'Jackie Robinson': {
        'valores': [0.474, 0.409, 0.311, 0.135, 0.075, 0.025, 0.883],
        'color': 'darkorchid'
    },
    'Jim Thome': {
        'valores': [0.554, 0.402, 0.276, 0.170, 0.280, 0.060, 0.956],
        'color': 'darkorange'
    },
    'Frank Thomas': {
        'valores': [0.555, 0.419, 0.301, 0.165, 0.170, 0.050, 0.974],
        'color': 'deepskyblue'
    }
}

# Crear la figura
fig = go.Figure()

# Agregar una trazo para cada grupo de datos
for nombre_grupo, data_grupo in datos.items():
    # Se añade el primer valor al final para cerrar el polígono del radar
    valores_circulares = data_grupo['valores'] + [data_grupo['valores'][0]]
    categorias_circulares = categorias + [categorias[0]] # Se cierra el polígono de categorías también
    
    color_linea = data_grupo['color']
    
    fig.add_trace(go.Scatterpolar(
        r=valores_circulares,
        theta=categorias_circulares,
        mode='lines+markers', 
        fill='none',     
        name=nombre_grupo,
        line_color=color_linea,  
        marker=dict(
            color=color_linea,
            size=8
        )
    ))

# Configurar el diseño del gráfico

fig.update_layout(
    title={
        'text': 'Estadísticas de Bateo MVP 2021 Shohei Ohtani vs Miembros del Salón de la Fama y Promedios 2021',
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 1.0]
        ),
        angularaxis=dict(
            tickfont_size=10,
        )
    ),
    showlegend=True,
    legend_title_text='Leyenda',
)

# Mostrar el gráfico
fig.show()