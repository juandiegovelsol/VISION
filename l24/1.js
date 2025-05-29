// Definimos las matrices de tu ejemplo:
const matrizA_ejemplo = [
  [1, 0, 0],
  [-1, 0, 3],
]; // Matriz 2x3
const matrizB_ejemplo = [
  [7, 0, 0],
  [0, 0, 0],
  [0, 0, 1],
]; // Matriz 3x3

/**
 * Realiza la multiplicación estándar de dos matrices A * B.
 * @param {number[][]} matrizA La primera matriz.
 * @param {number[][]} matrizB La segunda matriz.
 * @returns {number[][] | string} La matriz resultado o un mensaje de error si no se pueden multiplicar.
 */
function multiplicarMatrices(matrizA, matrizB) {
  const filasA = matrizA.length;
  const columnasA = matrizA[0].length;
  const filasB = matrizB.length;
  const columnasB = matrizB[0].length;

  // Comprobación: el número de columnas de A debe ser igual al número de filas de B.
  if (columnasA !== filasB) {
    return "No se pueden multiplicar: las columnas de la Matriz A no coinciden con las filas de la Matriz B.";
  }

  // La matriz resultado tendrá 'filasA' filas y 'columnasB' columnas.
  const matrizResultado = [];
  for (let i = 0; i < filasA; i++) {
    // Itera sobre las filas de la matriz A
    matrizResultado[i] = []; // Inicializa la fila i en la matriz resultado
    for (let j = 0; j < columnasB; j++) {
      // Itera sobre las columnas de la matriz B
      let sumaParcial = 0;
      // Bucle para calcular el producto punto de la fila i de A y la columna j de B
      for (let k = 0; k < columnasA; k++) {
        // columnasA es igual a filasB
        sumaParcial += matrizA[i][k] * matrizB[k][j];
      }
      matrizResultado[i][j] = sumaParcial;
    }
  }
  return matrizResultado;
}

// Probamos la función con tus matrices:
const miResultado = multiplicarMatrices(matrizA_ejemplo, matrizB_ejemplo);

// Mostramos los resultados.
console.log("Matriz A:", matrizA_ejemplo);
console.log("Matriz B:", matrizB_ejemplo);

if (typeof miResultado === "string") {
  console.error("Error:", miResultado);
} else {
  console.log("Resultado de la multiplicación:", miResultado);
  // Para tu ejemplo, esto imprimirá: [[7, 0, 0], [-7, 0, 3]]
}
