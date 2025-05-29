function calcularDescuento(precio, porcentaje) {
  // Validación de precio, debe ser un número positivo
  if (typeof precio !== "number" || precio <= 0) {
    throw new Error("El precio debe ser un número positivo");
  }
  // Validación de porcentaje, debe ser un número entre 0 y 100
  if (typeof porcentaje !== "number" || porcentaje <= 0 || porcentaje >= 100) {
    throw new Error("El porcentaje debe ser un número entre 0 y 100");
  }

  return precio - precio * (porcentaje / 100);
}

// Caso 1: Valores correctos
try {
  console.log(calcularDescuento(100, 20)); // 80
} catch (error) {
  console.error("Error:", error.message);
}

// Caso 2: Parámetro incorrecto (porcentaje negativo)
try {
  console.log(calcularDescuento(50, -20));
} catch (error) {
  console.error("Error:", error.message); // "El porcentaje debe ser un número entre 0 y 100"
}

// Caso 3: Ambos parámetros incorrectos
try {
  console.log(calcularDescuento("cien", 120));
} catch (error) {
  console.error("Error:", error.message); // "El precio debe ser un número positivo"
}
