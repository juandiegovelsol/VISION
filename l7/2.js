function isInteger(value) {
  return /^\d+$/.test(value);
}

const config = {
  min: parseInt(prompt("Ingresa el valor mínimo:")),
  max: parseInt(prompt("Ingresa el valor máximo:")),
};

const value = parseInt(prompt("Ingresa el valor actual:"));

if (!isInteger(config.min) || !isInteger(config.max) || !isInteger(value)) {
  console.log("Error: Solo se permiten números enteros.");
} else {
  if (value < config.min) {
    console.log("Yes");
  } else if (value > config.max) {
    console.log("No");
  } else {
    console.log("El valor está dentro del rango.");
  }
}
