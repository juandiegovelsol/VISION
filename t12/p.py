import matplotlib.pyplot as plt
import random
from matplotlib.widgets import Button

# Datos iniciales de la gráfica
categorias = ['Electricidad y calor', 'Transporte', 'Industria', 'Edificios', 'Otros']
valores = [49, 20, 20, 9, 2]  # Porcentajes

# Colores iniciales similares a los de la imagen
colores = ['#69b3cc', '#b3cc69', '#e6d267', '#cc6967', '#e6a067']

# Función para generar un color aleatorio
def color_aleatorio():
    return "#{:02x}{:02x}{:02x}".format(
        random.randint(100, 240),
        random.randint(100, 240),
        random.randint(100, 240)
    )

# Configuración del gráfico
fig, ax = plt.subplots(figsize=(10, 8))
fig.subplots_adjust(bottom=0.2)

# Creación del gráfico de anillo
wedges, texts, autotexts = ax.pie(
    valores, 
    labels=None,
    colors=colores,
    autopct='%1.0f%%',
    startangle=90,
    wedgeprops=dict(width=0.5, edgecolor='w'),
    textprops={'fontsize': 14, 'weight': 'bold', 'color': 'white'}
)

# Añadir un círculo blanco en el centro para crear el efecto de anillo
centro_circulo = plt.Circle((0, 0), 0.25, fc='white')
ax.add_patch(centro_circulo)

# Título
ax.set_title('EMISIONES DE CO2', fontsize=24, pad=20)

# Función para cambiar el color de una categoría específica al hacer clic
def cambiar_color(event, idx):
    nuevo_color = color_aleatorio()
    wedges[idx].set_facecolor(nuevo_color)
    colores[idx] = nuevo_color
    botones[idx].color = nuevo_color
    fig.canvas.draw_idle()

# Crear leyendas como botones
ax_botones = []
botones = []
for i, categoria in enumerate(categorias):
    # Posición del botón
    ax_btn = fig.add_axes([0.1 + i*0.165, 0.05, 0.15, 0.05])
    btn = Button(ax_btn, categoria, color=colores[i], hovercolor='0.9')
    btn.label.set_fontsize(10)
    btn.on_clicked(lambda event, idx=i: cambiar_color(event, idx))
    ax_botones.append(ax_btn)
    botones.append(btn)

plt.tight_layout()
plt.show()