const personas = [
  { nombre: "Juan", edad: 25 },
  { nombre: "María", edad: 30 },
  { nombre: "Pedro", edad: 40 },
];

function buscarPersona(nombre) {
  const persona = personas.find((persona) => persona.nombre === nombre);
  return persona ? persona : -1;
}

// Ejemplo de uso
console.log(buscarPersona("María")); // { nombre: 'María', edad: 30 }
console.log(buscarPersona("Ana")); // -1
