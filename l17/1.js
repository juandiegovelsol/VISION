const descuento = (valor) => {
  const dto = 0.05;
  const valorDto = valor - valor * dto;
  return valorDto;
};

const sumaIVA21 = (valor) => {
  const iva = 1.21;
  const total = valor * iva;
  return total;
};

// Array con las funciones que queremos concatenar
// Podemos añadir o quitar funciones según necesitemos
const calculaTotal = [descuento, sumaIVA21];

const reductor = (total, funcion) => {
  return funcion(total);
};

// suma total de producto del carrito
const sumaProductos = 100;

const totalCarrito = calculaTotal.reduce(reductor, sumaProductos);
console.log(totalCarrito); // 114.95
