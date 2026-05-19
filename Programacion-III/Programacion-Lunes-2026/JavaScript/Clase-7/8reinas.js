/**
 * N es el tamaño del tablero (N x N).
 */
function resolverNReinas(n) {
  // creamos un tablero vacío lleno de puntos (.)
  const tablero = Array.from({ length: n }, () => Array(n).fill("."));
  // este arreglo guardará la columna donde ubicamos la reina en cada fila
  const solucion = [];

  // función para verificar si es seguro poner una reina en una posición
  function esSeguro(fila, columna) {
    for (let i = 0; i < fila; i++) {
      const col = solucion[i];
      // 1. ¿tenemos otra reina en la misma columna?
      if (col === columna) return false;
      // 2. ¿hay otra reina en la misma diagonal? 
      // (si la diferencia de filas es igual a la de columnas, están en diagonal)
      if (Math.abs(col - columna) === Math.abs(i - fila)) return false;
    }
    return true;
  }

  // función para imprimir el tablero en la consola de forma legible
  function mostrarTablero(tablero) {
    console.log(tablero.map(fila => fila.join(" ")).join("\n"));
    console.log("-----------------");
  }

  // la función principal de backtracking
  function backtracking(fila) {
    // si llegamos a la fila N, significa que ubicamos todas las reinas bien
    if (fila === n) return true;

    for (let columna = 0; columna < n; columna++) {
      if (esSeguro(fila, columna)) {
        // ponemos a la reina
        solucion[fila] = columna;
        tablero[fila][columna] = "Q";

        console.log(`Probando la fila ${fila}, en la columna ${columna}:`);
        mostrarTablero(tablero);

        // hacemos la llamada recursiva: intentamos poner la reina en la siguiente fila
        if (backtracking(fila + 1)) return true;

        // si no funciona, quitamos la reina (backtracking) y probamos otra columna
        tablero[fila][columna] = ".";
        solucion[fila] = undefined;
      }
    }
    return false; // no se encontro ninguna solución en este camino
  }

  // iniciamos el proceso desde la fila 0
  if (backtracking(0)) {
    console.log("Encontramos la solucion final.");
    mostrarTablero(tablero);
    console.log("Arreglo de posiciones (índice = fila, valor = columna):", solucion);
  } else {
    console.log("No existe solución para este tamaño de tablero.");
  }
}

// ejecutamos el comando con las 8 reinas
resolverNReinas(8);
