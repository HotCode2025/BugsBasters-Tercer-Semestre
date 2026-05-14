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
let triunfos = 0 // Contador que acumulará las rondas ganadas por el jugador
let perdidas = 0 // Contador que acumulará las rondas ganadas por la PC (o perdidas por el jugador)
let juegoTerminado = false; // Variable para saber si el juego ya terminó

// Función principal que se ejecuta al presionar un botón
function jugar(jugador) {
    if (juegoTerminado) return; // Si el juego terminó, no hacer nada

    let pc = aleatorio(1, 3);
    let statusText = document.getElementById("status-text");

    // === LÓGICA DE COMBATE ===
    // Comparamos el valor de la computadora con el del jugador
    if (pc == jugador) {
        statusText.innerText = "Empate. PC eligió " + eleccion(pc) + ".";
    }
    else if (
        (jugador == 1 && pc == 3) || // Si el jugador es Piedra (1) y la PC es Tijera (3) -> Gana Piedra
        (jugador == 2 && pc == 1) || // Si el jugador es Papel (2) y la PC es Piedra (1) -> Gana Papel
        (jugador == 3 && pc == 2)    // Si el jugador es Tijera (3) y la PC es Papel (2) -> Gana Tijera
    ) {
        statusText.innerText = "¡Ganaste la ronda! PC eligió " + eleccion(pc) + ".";
        triunfos++;
        document.getElementById("score-jugador").innerText = triunfos;
    }
    else {
        statusText.innerText = "Perdiste la ronda. PC eligió " + eleccion(pc) + ".";
        perdidas++;
        document.getElementById("score-pc").innerText = perdidas;
    }

    // Comprobamos si alguien llegó a 3 victorias
    if (triunfos >= 3 || perdidas >= 3) {
        juegoTerminado = true;
        let mensajeFinal = (triunfos >= 3) ? "¡FELICIDADES! Ganaste la partida." : "¡FIN DEL JUEGO! La PC ganó.";
        statusText.innerText = mensajeFinal;
        statusText.style.fontWeight = "bold";
        statusText.style.color = (triunfos >= 3) ? "#48bb78" : "#f56565";
        
        // Cambiar el color del pulso para indicar el fin del juego
        let pulseDot = document.getElementById("pulse-dot");
        pulseDot.style.backgroundColor = (triunfos >= 3) ? "#48bb78" : "#f56565";
        
        // Deshabilitar botones
        document.getElementById("btn-rock").disabled = true;
        document.getElementById("btn-paper").disabled = true;
        document.getElementById("btn-scissors").disabled = true;

        // Mostrar botón de reinicio
        document.getElementById("btn-reset").style.display = "inline-block";
    }
}

// Función para reiniciar el juego
function reiniciar() {
    triunfos = 0;
    perdidas = 0;
    juegoTerminado = false;

    // Reiniciar marcadores en el HTML
    document.getElementById("score-jugador").innerText = "0";
    document.getElementById("score-pc").innerText = "0";

    // Reiniciar indicador de estado
    let statusText = document.getElementById("status-text");
    statusText.innerText = "Esperando jugadas...";
    statusText.style.fontWeight = "normal";
    statusText.style.color = "#e2e8f0";
    
    // Reiniciar el pulso a verde oscuro (color original)
    document.getElementById("pulse-dot").style.backgroundColor = "#48bb78";

    // Habilitar botones de juego
    document.getElementById("btn-rock").disabled = false;
    document.getElementById("btn-paper").disabled = false;
    document.getElementById("btn-scissors").disabled = false;

    // Ocultar botón de reinicio
    document.getElementById("btn-reset").style.display = "none";
}
