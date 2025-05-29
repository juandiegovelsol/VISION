import matplotlib.pyplot as plt

años = [2009, 2010, 2011, 2012, 2013]
impuestos = [505, 500, 500, 510, 520]

plt.plot(años, impuestos, marker='D', linestyle='-', color='blue')

plt.title('City Taxes', fontsize=16, fontweight='bold')
plt.xlabel('')  # No hay etiqueta para el eje x
plt.ylabel('Tax Amount (dollars)', fontsize=12, fontweight='bold')

plt.ylim(490, 525)

plt.grid(axis='y')  # Muestra solo las líneas horizontales de la cuadrícula
plt.show()