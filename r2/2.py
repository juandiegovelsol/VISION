import matplotlib.pyplot as plt

# Datos de ventas
años = ['93', '94', '95', '96', '97', '98', '99', '00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
ventas = [0.3, 0.6, 0.8, 1.1, 1.1, 1.4, 1.4, 1.5, 1.2, 1.3, 1.4, 1.2, 1.0, 0.9, 0.9, 1.8, 2.5, 2.8, 3.9, 4.6]

# Convertir años al formato AAAA
años_formateados = ['19' + año if int(año) > 12 else '20' + año for año in años]

# Crear la gráfica
plt.figure(figsize=(10, 6))
plt.bar(años_formateados, ventas, color='skyblue')
plt.title('Ventas de Discos de Vinilo en EE.UU.')
plt.xlabel('Años')
plt.ylabel('Número de Discos Vendidos por Año (M)')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Mostrar valores en la parte superior de cada barra
for i, venta in enumerate(ventas):
    plt.text(i, venta + 0.05, f'{venta}M', ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.show()