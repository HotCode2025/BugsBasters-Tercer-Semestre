function torresDeHanoi(n, origen, auxiliar, destino) {
    if (n === 1) {
        console.log(`Mover disco 1 de ${origen} a ${destino}`);
        return;
    }

    // Movemos n-1 discos de origen a auxiliar
    torresDeHanoi(n - 1, origen, destino, auxiliar);

    // Movemos el disco más grande a destino
    console.log(`Mover disco ${n} de ${origen} a ${destino}`);

    // Movemos n-1 discos de auxiliar a destino
    torresDeHanoi(n - 1, auxiliar, origen, destino);
}


const cantidadDiscos = 3;
torresDeHanoi(cantidadDiscos, 'A', 'B', 'C');
