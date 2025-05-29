from pycounts.pycounts import count_words
from pycounts.plotting import plot_words
import matplotlib.pyplot as plt

# Texto simulado 
text = """
apple banana orange grape kiwi mango peach lemon pear plum
banana apple orange apple banana plum peach kiwi grape mango
lemon pear apple banana mango plum orange peach grape kiwi
"""

# Guardar el texto en un archivo temporal
with open("temp.txt", "w") as f:
    f.write(text)

# Usar la función como en el ejemplo
file_path = "temp.txt"
counts = count_words(file_path)
fig = plot_words(counts, n=10)
plt.show()