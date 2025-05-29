import matplotlib.pyplot as plt
import pandas as pd

# Datos de patentes
anos = list(range(2000, 2022))
baterias = [9500, 9500, 9000, 9500, 11000, 12500, 14000, 16500, 18500, 25000, 30500, 32500, 33500, 34500, 37000, 39000, 45000, 53000, 61000, 60500, 53000, 14000]
almacenamiento_general = [500, 500, 800, 1600, 1700, 1900, 2700, 2800, 3350, 3600, 3800, 4000, 5100, 5300, 5500, 5600, 5700, 5000, 5300, 5900, 6300, 2300]
alm_sin_baterias = [300, 300, 400, 500, 600, 800, 1000, 1100, 1300, 1500, 1600, 1800, 2000, 2200, 2300, 2400, 2600, 2900, 2700, 3800, 4200, 1100]
alm_energia_termica = [150, 150, 150, 150, 200, 250, 300, 350, 400, 500, 600, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 400]

# Crear el DataFrame
df = pd.DataFrame({
    "Año": anos,
    "Baterías": baterias,
    "Almacenamiento (general)": almacenamiento_general,
    "Almacenamiento (excl. baterías)": alm_sin_baterias,
    "Almacenamiento de energía térmica": alm_energia_termica
})

# Definir colores
colors = ["#c05020", "#8eb694", "#5a7ca3", "#3b4b74"]
labels = [
    "Baterías",
    "Almacenamiento (general)",
    "Almacenamiento (excl. baterías)",
    "Almacenamiento de energía térmica"
]
data_columns = [
    "Baterías",
    "Almacenamiento (general)",
    "Almacenamiento (excl. baterías)",
    "Almacenamiento de energía térmica"
]

# Gráfico de barras superpuestas
plt.figure(figsize=(12, 8))

# Graficar las barras en orden de mayor a menor para que las más pequeñas queden al frente
plt.bar(df["Año"], df["Baterías"], label=labels[0], color=colors[0], width=0.8)
plt.bar(df["Año"], df["Almacenamiento (general)"], label=labels[1], color=colors[1], width=0.8)
plt.bar(df["Año"], df["Almacenamiento (excl. baterías)"], label=labels[2], color=colors[2], width=0.8)
plt.bar(df["Año"], df["Almacenamiento de energía térmica"], label=labels[3], color=colors[3], width=0.8)

# Títulos y etiquetas
plt.title("Patentes anuales registradas para tecnologías de almacenamiento de energía en el mundo", fontsize=14)
plt.xlabel("Año")
plt.ylabel("Número de patentes")

# Leyendas
plt.legend(loc="upper left")

plt.grid(True, axis='y', linestyle='--', alpha=0.6)
plt.xticks(anos[::2]) # Mostrar años de 2 en 2 para evitar solapamiento en el eje x
plt.show()