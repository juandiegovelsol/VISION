import matplotlib.pyplot as plt
import numpy as np

# Datos de ejemplo (necesitarás reemplazar estos con tus datos reales)
anos = np.arange(1979, 2023)
hielo_marino = np.random.normal(3, 0.5, len(anos))  # Datos de ejemplo

plt.figure(figsize=(10, 6))
plt.plot(anos, hielo_marino, marker='o')

# Ajuste del rango del eje Y a los datos
plt.ylim(min(hielo_marino) - 0.5, max(hielo_marino) + 0.5)

# Ajuste de los ticks del eje X cada 5 años
plt.xticks(np.arange(1980, 2026, 5))

# Títulos y etiquetas en español
plt.title('Mínimo Anual de Hielo Marino en la Antártida', fontsize=16)
plt.xlabel('Años', fontsize=14)
plt.ylabel('Extensión mínima de hielo marino antártico\n(millones de km²)', fontsize=14)

plt.grid(True)
plt.tight_layout()
plt.show()