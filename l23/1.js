import ESDoc from "esdoc/src/ESDoc.js";

let config = {
  source: "./src", // carpeta con tu código fuente
  destination: "./esdoc", // carpeta donde se generará la documentación
};

// Renombramos el callback para evitar sombreado de 'config'
ESDoc.generate(config, (onComplete) => {
  console.log(onComplete); // estadísticas y advertencias de generación
});
