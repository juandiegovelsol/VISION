/**
 * Calcula el alcance horizontal de un tiro parabólico.
 *
 * @param {number} v0 Velocidad inicial en m/s (debe ser > 0).
 * @param {number} alphaDeg Ángulo de lanzamiento en grados (entre 0 y 90, excluidos).
 * @returns {number} Posición final en metros.
 * @throws {TypeError} Si algún parámetro no es numérico.
 * @throws {RangeError} Si algún parámetro no es positivo o el ángulo no está en rango.
 */
function calcularAlcance(v0, alphaDeg) {
  // Constante de gravedad en sistema internacional de medida
  const G = 9.81;
  // Validación de tipos
  if (typeof v0 !== "number" || typeof alphaDeg !== "number") {
    throw new TypeError("Todos los parámetros deben ser números.");
  }
  // Validación de rango
  if (v0 <= 0) {
    throw new RangeError(
      "La velocidad inicial v0 debe ser un número positivo."
    );
  }
  if (alphaDeg <= 0 || alphaDeg >= 90) {
    throw new RangeError(
      "El ángulo alpha debe estar entre 0° y 90° (no incluidos)."
    );
  }

  // Conversión a radianes
  const alphaRad = (alphaDeg * Math.PI) / 180;

  // Fórmula del alcance: R = v0^2 * sin(2α) / G
  const alcance = (v0 * v0 * Math.sin(2 * alphaRad)) / G;

  return alcance.toFixed(2);
}

// Ejemplo de uso:
try {
  const v0 = 20; // m/s
  const angulo = 45; // grados
  const rango = calcularAlcance(v0, angulo);
  console.log(`El proyectil recorre ${rango} m antes de volver a y = 0.`);
} catch (err) {
  console.error(err.message);
}
