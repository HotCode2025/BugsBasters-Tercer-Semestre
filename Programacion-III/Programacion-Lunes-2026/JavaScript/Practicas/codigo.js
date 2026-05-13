// Función matemática para generar un número aleatorio entero entre un mínimo y un máximo incluyéndolos
function aleatorio(min, max) {
    return Math.floor(Math.random() * (max - min + 1) + min);
}

// Función que convierte el número elegido (1, 2 o 3) en una palabra descriptiva
function eleccion(jugada) {
    let resultado = "" // Inicializamos un texto vacío
    
    // Evaluamos qué número llegó como parámetro
    if (jugada == 1) {
        resultado = "piedra"
    }
    else if (jugada == 2) {
        resultado = "papel"
    }
    else if (jugada == 3) {
        resultado = "tijera"
    }
    else {
        resultado = "perdio" // Si el jugador ingresa una letra u otro número, por defecto pierde esa ronda
    }
    return resultado // Devolvemos la palabra correspondiente
}

// === DECLARACIÓN DE VARIABLES INICIALES ===
// Regla del juego: 1 será piedra, 2 será papel, 3 será tijera
let jugador = 0 // Almacena la jugada elegida por el usuario
let pc = 0 // Almacena la jugada aleatoria de la computadora
let min = 1 // Valor mínimo para generar el número aleatorio de la PC
let max = 3 // Valor máximo para generar el número aleatorio de la PC
let triunfos = 0 // Contador que acumulará las rondas ganadas por el jugador
let perdidas = 0 // Contador que acumulará las rondas ganadas por la PC (o perdidas por el jugador)


// Bucle while: el juego se repite continuamente MIENTRAS el jugador NO tenga 3 victorias Y la PC NO tenga 3 victorias
while (triunfos < 3 && perdidas < 3) {
    
    // La computadora elige un número al azar entre 1 y 3 usando nuestra función
    pc = aleatorio(1, 3)
    
    // Le pedimos al jugador que escriba y guarde su elección mediante un cuadro de diálogo
    jugador = prompt("ELIGE : 1 piedra, 2 papel, 3 tijera ");

    // Mostramos mediante ventanas de alerta qué escogió cada uno, usando la función 'eleccion' para mostrar texto en vez del número
    alert("pc eligio " + eleccion(pc))
    alert("jugador eligio " + eleccion(jugador))

    // === LÓGICA DE COMBATE ===
    // Comparamos el valor de la computadora con el del jugador
    if (pc == jugador) {
        // Si eligieron el mismo número, declaran empate (los puntos no cambian)
        alert("empate")
    }
    else if (
        (jugador == 1 && pc == 3) || // Si el jugador es Piedra (1) y la PC es Tijera (3) -> Gana Piedra
        (jugador == 2 && pc == 1) || // Si el jugador es Papel (2) y la PC es Piedra (1) -> Gana Papel
        (jugador == 3 && pc == 2)    // Si el jugador es Tijera (3) y la PC es Papel (2) -> Gana Tijera
    ) {
        // Si se cumple ALGUNA (||) de las 3 condiciones de arriba, el jugador gana la ronda
        alert("gana jugador")
        triunfos++ // Sumamos 1 al marcador de victorias del jugador
    }
    else {
        // Si no fue empate y no se cumplió ninguna condición para que gane el jugador, lógicamente gana la PC
        alert("perdiste jugador")
        perdidas++ // Sumamos 1 al marcador de derrotas del jugador
    }
} // Fin del bucle: si alguien llega a 3, el bucle se detiene

// Cuando salimos del bucle (alguien llegó a 3 puntos), mostramos una alerta final con el resultado general
alert("ganaste: " + triunfos + " veces. perdiste: " + perdidas + " veces")
