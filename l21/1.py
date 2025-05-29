import matplotlib.pyplot as plt

# Datos
años = [2002, 2004, 2006, 2007, 2008, 2009, 2011, 2012]
total_secretarios = [27, 25, 31, 25, 32, 32, 31, 22]
mujeres = [7, 3, 6, 5, 9, 8, 6, 4]
porcentaje_mujeres = [m/t*100 for m, t in zip(mujeres, total_secretarios)]

# Crear figura y ejes
fig, ax = plt.subplots(figsize=(12, 6))

# Barras para el total de secretarios
ax.bar(años, [t - m for t, m in zip(total_secretarios, mujeres)], color='silver', label='Hombres')

# Barras para mujeres (apiladas sobre el total)
bars_mujeres = ax.bar(años, mujeres, 
                      bottom=[t - m for t, m in zip(total_secretarios, mujeres)], 
                      color='darksalmon', label='Mujeres')

# Añadir porcentajes encima de las barras de mujeres
for i, (m, pct) in enumerate(zip(mujeres, porcentaje_mujeres)):
    # Calcular la posición vertical (top de la barra de mujeres)
    pos_m = total_secretarios[i] - mujeres[i] + mujeres[i] + 0.3
    ax.text(años[i], pos_m, f'{pct:.1f}%', ha='center', va='bottom', fontsize=9, fontweight='bold')

# Leyenda del gráfico
ax.set_title('TOTAL DE NOMBRAMIENTOS: SECRETARIOS / SECRETARIAS DE ESTADO', pad=20, fontweight='bold')
ax.set_xlabel('Año')
ax.set_ylabel('Número de Nombramientos')
ax.set_xticks(años)
ax.legend()

# Mostrar el gráfico
plt.tight_layout()
plt.show()