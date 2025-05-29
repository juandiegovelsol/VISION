import matplotlib.pyplot as plt

años = [2009, 2010, 2011, 2012, 2013]
impuestos = [505, 500, 500, 510, 520]

plt.plot(años, impuestos, marker='D', linestyle='-', color='blue')

# Título y etiquetas en negrita
plt.title('Impuestos municipales', fontsize=18, fontweight='bold') 
plt.ylabel('Monto del impuesto (dólares)', fontsize=10, fontweight='bold')    

# Configurar el eje X para mostrar únicamente los años como etiquetas
plt.xticks(años)

# Límites del eje y para que coincida visualmente
plt.ylim(490, 525)

# Mostrar el gráfico
plt.grid(axis='y') # Incluir solo las líneas horizontales
plt.show()