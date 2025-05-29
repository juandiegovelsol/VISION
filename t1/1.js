// Declaramos variables

var x = 1;
var y = 2;

// Definimos funciones para operaciones aritméticas

const suma = (x, y) => {
  // Validamos el tipo de los parámetros
  if (typeof x !== "number" || typeof y !== "number") {
    return "Los parámetros deben ser números";
  }
  // Se produce el resultado de la suma
  return `El resultado de la suma es: ${x + y}`;
};

const resta = (x, y) => {
  // Validamos el tipo de los parámetros
  if (typeof x !== "number" || typeof y !== "number") {
    return "Los parámetros deben ser números";
  }
  // Se produce el resultado de la resta
  return `El resultado de la resta es: ${x - y}`;
};

const multiplicacion = (x, y) => {
  // Validamos el tipo de los parámetros
  if (typeof x !== "number" || typeof y !== "number") {
    return "Los parámetros deben ser números";
  }
  // Se produce el resultado de la multiplicación
  return `El resultado de la multiplicación es: ${x * y}`;
};

const division = (x, y) => {
  // Validamos el tipo de los parámetros
  if (typeof x !== "number" || typeof y !== "number") {
    return "Los parámetros deben ser números";
  }
  // Validamos que el dividendo sea diferente de cero
  if (y === 0) {
    return "El dividendo no puede ser cero";
  }
  // Se produce el resultado de la división
  return `El resultado de la división es ${x / y}`;
};

// Ejemplos de uso para cada función
console.log(suma(x, y));
console.log(resta(x, y));
console.log(multiplicacion(x, y));
console.log(division(x, y));
