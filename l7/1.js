const minInput = prompt("Ingrese el valor mínimo (entero):");
const maxInput = prompt("Ingrese el valor máximo (entero):");
const valueInput = prompt("Ingrese el valor a evaluar (entero):");

if (
  !Number.isInteger(Number(minInput)) ||
  !Number.isInteger(Number(maxInput)) ||
  !Number.isInteger(Number(valueInput))
) {
  console.error("Error: Todos los valores deben ser números enteros");
} else {
  const config = {
    min: Number(minInput),
    max: Number(maxInput),
  };

  const value = Number(valueInput);

  if (value < config.min) {
    console.log("Si");
  } else if (value > config.max) {
    console.log("No");
  }
}
