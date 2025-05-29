import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import matplotlib.ticker as ticker


años = np.array([
    1950, 1955, 1960, 1965, 1970, 1975, 1980, 1985, 1990, 1995, 
    2000, 2005, 2010, 2015, 2020, 2025, 2030, 2035, 2040, 2045, 2050
]).reshape(-1, 1)


poblacion = np.array([
    15000, 18000, 23000, 28000, 35000, 45000, 58000, 70000, 85000, 110000, 
    130000, 170000, 200000, 250000, 300000, 370000, 425000, 490000, 570000, 640000, 710000
])

# Cálculo de estadísticas
media = np.mean(poblacion)
mediana = np.median(poblacion)
print(f"Media de la población: {media:,.2f} miles de personas")
print(f"Mediana de la población: {mediana:,.2f} miles de personas")

# Regresión lineal para calcular la tendencia
modelo = LinearRegression()
modelo.fit(años, poblacion)
pendiente = modelo.coef_[0]  
intercepto = modelo.intercept_
print(f"Pendiente de la línea de tendencia: {pendiente:,.2f} miles de personas por año")
print(f"Intercepto: {intercepto:,.2f}")
print(f"Ecuación de la línea: y = {pendiente:.2f}x + {intercepto:.2f}")

# Configuración de la figura con el tamaño exacto para replicar la proporción de la imagen
plt.figure(figsize=(12, 8))
plt.style.use('default')  

# Configurar el fondo blanco
plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['figure.facecolor'] = 'white'

# Crear la gráfica con un eje para controlar mejor los elementos
ax = plt.subplot(111)

# Líneas de cuadrícula horizontales con estilo punteado gris claro
ax.yaxis.grid(True, linestyle=':', color='lightgray', alpha=0.8)
ax.set_axisbelow(True)  


ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_color('lightgray')

# Configurar los límites del eje y
ax.set_ylim(0, 1000000)
ticks_y = [0, 100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000]
labels_y = ['0', '100.000', '200.000', '300.000', '400.000', '500.000', '600.000', '700.000', '800.000', '900.000', '1.000.000']
ax.set_yticks(ticks_y)
ax.set_yticklabels(labels_y)


ax.set_xlim(1950, 2050)
ax.set_xticks([1950, 2025])
ax.set_xticklabels(['1950', '2025'], fontsize=9)
plt.xticks(rotation=45)


for tick in ax.get_xticklabels():
    tick.set_rotation(45)
    tick.set_ha('right')


ax.set_ylabel('Personas (Miles)', fontsize=10, labelpad=10)
ax.tick_params(axis='y', which='major', labelsize=9)


plt.plot(años, poblacion, 'o-', color='#F5A623', linewidth=1.5, markersize=5, 
         markeredgecolor='#F5A623', markerfacecolor='#F5A623')


plt.title('Evolución de la población mayor de 80 años en el mundo', fontsize=18, fontweight='bold', pad=20)


plt.figtext(0.455, 0.01, 'Personas (miles)', fontsize=9, color='#F5A623',
            bbox=dict(facecolor='white', edgecolor='white', boxstyle='square,pad=0'))
plt.figtext(0.43, 0.01, '■', fontsize=12, color='#F5A623', ha='right')


plt.figtext(0.84, 0.01, 'Fuente: ONU, www.epdata.es', fontsize=9, ha='right')


plt.tight_layout(rect=[0, 0.03, 1, 0.97])
plt.subplots_adjust(bottom=0.1)


plt.figure(figsize=(10, 6))
plt.scatter(años, poblacion, color='#F5A623', label='Datos originales')


años_rango = np.array([[1950], [2050]])
prediccion = modelo.predict(años_rango)
plt.plot(años_rango, prediccion, color='blue', linewidth=2, 
         label=f'Línea de regresión (y = {pendiente:.2f}x + {intercepto:.2f})')

plt.title('Evolución de la población mayor de 80 años con línea de tendencia', fontsize=14)
plt.xlabel('Año', fontsize=12)
plt.ylabel('Población (miles)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.savefig('poblacion_con_regresion.png', dpi=300)


plt.figure(1)
plt.savefig('poblacion_mayores_80.png', dpi=300, bbox_inches='tight')
plt.show()

indice_2025 = np.where(años.flatten() == 2025)[0][0]
print(f"Valor en 2025: {poblacion[indice_2025]:,} miles de personas")

# Calcular tasa de crecimiento
valor_inicial = poblacion[0]  # 1950
valor_final = poblacion[-1]   # 2050
tasa_crecimiento = ((valor_final / valor_inicial) ** (1/100)) - 1  # 100 años
print(f"Tasa de crecimiento anual promedio: {tasa_crecimiento*100:.2f}%")

# Calcular coeficiente de determinación (R²)
predicciones = modelo.predict(años)
ss_total = np.sum((poblacion - np.mean(poblacion)) ** 2)
ss_residual = np.sum((poblacion - predicciones) ** 2)
r_cuadrado = 1 - (ss_residual / ss_total)
print(f"Coeficiente de determinación (R²): {r_cuadrado:.4f}")

# Análisis por períodos
print("\nAnálisis por períodos:")
periodos = [
    (1950, 1975, "1950-1975"), 
    (1975, 2000, "1975-2000"),
    (2000, 2025, "2000-2025"),
    (2025, 2050, "2025-2050 (proyección)")
]

for inicio, fin, nombre in periodos:
    idx_inicio = np.where(años.flatten() == inicio)[0][0]
    idx_fin = np.where(años.flatten() == fin)[0][0]
    pob_inicio = poblacion[idx_inicio]
    pob_fin = poblacion[idx_fin]
    cambio_pct = ((pob_fin / pob_inicio) - 1) * 100
    print(f"  {nombre}: {pob_inicio:,} a {pob_fin:,} miles ({cambio_pct:.1f}% de cambio)")