// 1. Definimos las variables necesarias
const n = 8; // Tamaño del tablero
const tablero = Array.from({ length: n }, () => Array(n).fill(0));
const movimientos = [
  [2, 1], [1, 2], [-1, 2], [-2, 1],
  [-2, -1], [-1, -2], [1, -2], [2, -1]
];

// 2. Función recursiva
function resolver(x, y, paso) {
  // Marca la casilla actual con el número de paso
  tablero[x][y] = paso;

  // Si ya visitamos todas las casillas (n*n), terminamos
  if (paso === n * n) {
    return true;
  }

  // Aqui probamos los 8 movimientos
  for (const [dx, dy] of movimientos) {
    const nx = x + dx;
    const ny = y + dy;

    // Comprobamos si el movimiento es válido y no visitado
    if (nx >= 0 && nx < n && ny >= 0 && ny < n && tablero[nx][ny] === 0) {
      if (resolver(nx, ny, paso + 1)) {
        return true;
      }
    }
  }

  // Backtracking: si no hay salida, liberamos a la casilla
  tablero[x][y] = 0;
  return false;
}

// 3. Ejecutamos
console.log("Calculando el salto del caballo...");

if (resolver(0, 0, 1)) {
  console.log("¡Solución encontrada!");
  // Imprimimos el tablero de forma legible
  tablero.forEach(fila => {
    console.log(fila.map(num => String(num).padStart(2, '0')).join(' | '));
  });
} else {
  console.log("No se encontró solución para este tablero.");
}
