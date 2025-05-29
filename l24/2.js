function multiplyMatrices(A, B) {
  let rowsA = A.length,
    colsA = A[0].length,
    rowsB = B.length,
    colsB = B[0].length;
  let result = new Array(rowsA); // Matriz resultado

  for (let i = 0; i < rowsA; i++) {
    result[i] = new Array(colsB).fill(0); // Inicializar las filas de resultado
    for (let j = 0; j < colsB; j++) {
      for (let k = 0; k < colsA; k++) {
        result[i][j] += A[i][k] * B[k][j];
      }
    }
  }
  return result;
}

let A = [
  [1, 0, 0],
  [-1, 0, 3],
];

let B = [
  [7, 0, 0],
  [0, 0, 0],
  [0, 0, 1],
];

let C = multiplyMatrices(A, B);
console.log(C);
