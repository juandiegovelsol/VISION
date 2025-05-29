import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

# Datos aproximados extraídos de la imagen, reemplazalos por datos más exactos
years = np.array([1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023])
ice_extent = np.array([3.1, 2.8, 2.8, 3.1, 2.9, 2.7, 3.2, 3.0, 2.9, 3.2, 2.9, 2.5, 2.7, 3.1, 3.5, 2.5, 3.0, 2.9, 3.3, 3.5, 3.0, 3.6, 3.0, 3.8, 3.6, 2.9, 2.6, 3.2, 2.7, 3.0, 3.2, 3.9, 3.0, 2.5, 3.0, 3.8, 3.8, 3.8, 2.3, 2.4, 2.8, 3.0, 2.9, 2.2, 1.9])

# Crear la figura y los ejes
fig, ax = plt.subplots(figsize=(10, 6))

# Trazar los datos
ax.plot(years, ice_extent, marker='', linestyle='-')

# Ajustar el eje Y para tener ticks enteros
ax.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))

# Ajustar el eje X con saltos de 5 años desde 1980
start_year_tick = 1980
end_year_tick = years.max()
ax.set_xticks(np.arange(start_year_tick, end_year_tick + 1, 5))

# Configurar etiquetas y título en español
ax.set_xlabel('Años', fontsize=12)
ax.set_ylabel('Extensión mínima anual del hielo marino antártico (millones de km²)', fontsize=12)
ax.set_title('MÍNIMO ANUAL DEL HIELO MARINO ANTÁRTICO', fontsize=16, color='#4682B4', loc='left') # Alinear el título a la izquierda

# Añadir cuadrícula
ax.grid(True, linestyle='-', alpha=0.6)

# Eliminar el borde superior y derecho del gráfico para que se parezca más al original
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Mostrar el gráfico
plt.tight_layout() # Ajustar el layout para que no se corten las etiquetas
plt.show()