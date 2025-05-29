const personas = [
  { nombre: "Juan", edad: 25 },
  { nombre: "María", edad: 30 },
  { nombre: "Pedro", edad: 40 },
];

function buscarPorNombre(nombre) {
  // Usamos find con la condición de que el nombre que esta el arreglo es igual al nombre que recibe la función
  const encontrado = personas.find((persona) => persona.nombre === nombre);

  // Regresamos el objeto de la persona que tiene ese nombre, si no regresará -1
  return encontrado ? encontrado : -1;
}

// Ejemplos de uso
console.log(buscarPorNombre("Pedro")); // Esto imprimirá { nombre: "Pedro", edad: 40 }
console.log(buscarPorNombre("Carlos")); // Esto imprimirá -1
