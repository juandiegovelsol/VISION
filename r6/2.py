import random
import tempfile
from pycounts.pycounts import count_words
from pycounts.plotting import plot_words
import matplotlib.pyplot as plt

# Generar lista de palabras aleatorias
palabras = ["python", "code", "function", "data", "example", "list", "random", "text", "file"] * 10

# Crear un archivo temporal y escribir las palabras en él
with tempfile.NamedTemporaryFile(delete=False, mode='w') as temp_file:
    file_path = temp_file.name
    temp_file.write(' '.join(palabras))

# Contar palabras y graficar
counts = count_words(file_path)
fig = plot_words(counts, n=10)
plt.show()