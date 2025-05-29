import matplotlib.pyplot as plt

# Definición de los datos en listas
years = list(range(2000, 2023))

# Valores aproximados de huella material mundial (kg por € de PIB)
world_data = [
    1.18, 1.17, 1.175, 1.18, 1.19, 1.195, 1.195,
    1.20, 1.18, 1.19, 1.21, 1.225, 1.235, 1.24,
    1.22, 1.18, 1.15, 1.13, 1.10, 1.07, 1.10,
    1.13, 1.12
]

# Valores para España (kg por € de PIB)
spain_data = [
    0.95, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99,
    1.00, 0.98, 0.99, 1.02, 1.03, 1.04, 1.05,
    1.03, 0.97, 0.94, 0.92, 0.89, 0.87, 0.90,
    0.93, 0.92
]

# Creación de la figura
plt.figure(figsize=(10, 6))

# Trazado de ambas series
plt.plot(years, world_data, marker='o', label='Mundo')
plt.plot(years, spain_data, marker='o', label='España')

# Ajustes de estilo
plt.title('Huella material por PIB (kg/€), 2000–2022')
plt.xlabel('Año')
plt.ylabel('kg/€')
plt.xticks(years, rotation=45)
plt.ylim(0, max(max(world_data), max(spain_data)) * 1.1)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.legend()

# Mostrar el gráfico
plt.tight_layout()
plt.show()
