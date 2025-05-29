import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Definición de datos de ejemplo
dias_semana = ['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom']
manzanas_consumidas = [2, 8, 11, 7, 2, 4, 3]
consumo_energia_kj = [5700, 5500, 8200, 8900, 5000, 5800, 6600] # En Kilojoules (kJ)

# Crear la figura con un eje Y secundario
fig = make_subplots(specs=[[{"secondary_y": True}]])

# Añadir la serie de Manzanas (gráfico de barras)
fig.add_trace(
    go.Bar(
        x=dias_semana,
        y=manzanas_consumidas,
        name='Manzanas',
        marker_color='mediumseagreen',
        opacity=0.8
    ),
    secondary_y=False, # Este gráfico va en el eje Y primario (izquierda)
)

# Añadir la serie de Consumo de Energía (gráfico de línea curva)
fig.add_trace(
    go.Scatter(
        x=dias_semana,
        y=consumo_energia_kj,
        name='Consumo Total de Energía (kJ)',
        mode='lines+markers',
        line=dict(color='darkviolet', width=2.5, shape='spline'),
        marker=dict(color='darkviolet', size=8, line=dict(color='white', width=1))
    ),
    secondary_y=True, # Este gráfico va en el eje Y secundario (derecha)
)

# Configurar el diseño del gráfico (títulos, ejes, leyenda, etc.)
fig.update_layout(
    title_text="Manzanas consumidas comparado con el consumo total de energía diario",
    xaxis_title="Día de la semana",
    legend_title_text="Leyenda",
    plot_bgcolor='white',
    # Configuración de las leyendas
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="center",
        x=0.5
    )
)

# Configuración del eje Y primario (Manzanas)
fig.update_yaxes(
    title_text="Cantidad de Manzanas",
    secondary_y=False,
    showgrid=True, gridwidth=1, gridcolor='LightGrey',
    zeroline=True, zerolinewidth=1, zerolinecolor='Gainsboro',
    tickvals=[0, 2, 4, 6, 8, 10, 12],
    ticktext=["0 Manzanas", "2 Manzanas", "4 Manzanas", "6 Manzanas", "8 Manzanas", "10 Manzanas", "12 Manzanas"],
    range=[0, 12.5]
)

# Configuración del eje Y secundario (Energía)
fig.update_yaxes(
    title_text="Consumo Total de Energía (kJ)",
    secondary_y=True,
    showgrid=False,
    zeroline=False,
    tickvals=[0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000],
    range=[0, 9500] 
)

# Configurar la cuadrícula del eje X
fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGrey')


# Mostrar el gráfico
fig.show()