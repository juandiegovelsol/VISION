import matplotlib.pyplot as plt
import pandas as pd

# Datos de patentes
anos = list(range(2000, 2022))
baterias = [9500, 9500, 9000, 9500, 11000, 12500, 14000, 16500, 18500, 25000, 30500, 32500, 33500, 34500, 37000, 39000, 45000, 53000, 61000, 60500, 53000, 14000]
almacenamiento_general = [500, 500, 600, 600, 700, 900, 1100, 1200, 1350, 1600, 1800, 2000, 2100, 2300, 2500, 2600, 2700, 3000, 3300, 3900, 4300, 1300]
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

# Gráfico de barras apiladas
plt.figure(figsize=(12, 8))
plt.stackplot(
    df["Año"],
    df["Baterías"],
    df["Almacenamiento (general)"],
    df["Almacenamiento (excl. baterías)"],
    df["Almacenamiento de energía térmica"],
    labels=[
        "Baterías",
        "Almacenamiento (general)",
        "Almacenamiento (excl. baterías)",
        "Almacenamiento de energía térmica"
    ],
    colors=["#c05020", "#8eb694", "#5a7ca3", "#3b4b74"]
)

plt.title("Patentes anuales registradas para tecnologías de almacenamiento de energía en el mundo", fontsize=14)
plt.suptitle("Las cifras de los últimos años están sujetas a demoras; las patentes presentadas pueden no estar reflejadas aún en los datos.", fontsize=10, y=0.91)
plt.xlabel("Año")
plt.ylabel("Número de patentes")
plt.legend(loc="upper left")
plt.grid(True, axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
