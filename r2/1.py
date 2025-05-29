import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

anios_dos_digitos = list(range(93, 100)) + list(range(0, 13))  # 93–99 y 00–12

# Convertir cada año al formato AAAA
anios = []
for a in anios_dos_digitos:
    if 0 <= a <= 12:
        anios.append(2000 + a)
    else:
        anios.append(1900 + a)

# Valore de las ventas
ventas_millones = [
    0.3, 0.6, 0.8, 1.1, 1.1, 1.4, 1.4, 1.5,
    1.2, 1.3, 1.4, 1.2, 0.9, 0.9, 1.0, 1.8,
    2.5, 2.8, 3.9, 4.6
]

ventas = [v * 1_000_000 for v in ventas_millones]

# Crear gráfico
plt.figure(figsize=(12, 6))
barras = plt.bar(anios, ventas, color='steelblue', edgecolor='black')

# Etiquetas de los ejes
plt.title("Ventas de Discos de Vinilo en EE.UU. (1993–2012)", fontsize=14)
plt.xlabel("Año", fontsize=12)
plt.ylabel("Número de discos vendidos por año", fontsize=12)

formatter = ticker.FuncFormatter(lambda x, pos: f'{x / 1_000_000:.0f}M')
plt.gca().yaxis.set_major_formatter(formatter)
plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(1_000_000))
plt.xticks(anios, rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Mostrar valores encima de cada barra 
for bar, valor in zip(barras, ventas_millones):
    altura = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, altura + 100_000,
             f'{valor:.1f}M', ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.show()