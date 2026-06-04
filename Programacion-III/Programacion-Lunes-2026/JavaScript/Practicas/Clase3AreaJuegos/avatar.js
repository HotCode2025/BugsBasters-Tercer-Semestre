let ataqueJugador
let ataqueEnemigo

function seleccionarPersonajeJugador() {
    let inputZuko = document.getElementById('zuko')
    let inputKatara = document.getElementById('katara')
    let inputAang = document.getElementById('aang')
    let inputToph = document.getElementById('toph')
    
    let spanPersonajeJugador = document.getElementById('personaje-jugador')

    if (inputZuko.checked) {
        spanPersonajeJugador.innerHTML = 'Zuko'
    } else if (inputKatara.checked) {
        spanPersonajeJugador.innerHTML = 'Katara'
    } else if (inputAang.checked) {
        spanPersonajeJugador.innerHTML = 'Aang'
    } else if (inputToph.checked) {
        spanPersonajeJugador.innerHTML = 'Toph'
    } else {
        alert('DEBES SELECCIONAR UN PERSONAJE')
        return 
    }

    seleccionarPersonajeEnemigo()
}

function seleccionarPersonajeEnemigo() {
    let personajeAleatorio = aleatorio(1, 4) 
    let spanPersonajeEnemigo = document.getElementById('personaje-enemigo')

    if(personajeAleatorio == 1) {
        spanPersonajeEnemigo.innerHTML = 'Zuko'
    } else if(personajeAleatorio == 2) {
        spanPersonajeEnemigo.innerHTML = 'Katara'
    } else if(personajeAleatorio == 3) {
        spanPersonajeEnemigo.innerHTML = 'Aang'
    } else {
        spanPersonajeEnemigo.innerHTML = 'Toph'
    }
}

function aleatorio(min, max) {
    return Math.floor(Math.random() * (max - min + 1) + min);
}

function ataquePunio() {
    ataqueJugador = 'PUÑO'
    alert(ataqueJugador)
    seleccionarAtaqueEnemigo() // <-- Llamamos al nuevo nombre de la función
}

function ataquePatada() {
    ataqueJugador = 'PATADA'
    alert(ataqueJugador)
    seleccionarAtaqueEnemigo() // <-- Llamamos al nuevo nombre de la función
}

function ataqueBarrida() {
    ataqueJugador = 'BARRIDA'
    alert(ataqueJugador)
    seleccionarAtaqueEnemigo() // <-- Llamamos al nuevo nombre de la función
}

// Le cambiamos el nombre a la función para que no choque con la variable
function seleccionarAtaqueEnemigo() {
    let ataqueAleatorio = aleatorio(1, 3)
    if(ataqueAleatorio == 1) {
        ataqueEnemigo = 'PUÑO' // Aquí guardamos el texto en la variable
    } else if(ataqueAleatorio == 2) {
        ataqueEnemigo = 'PATADA'
    } else {
        ataqueEnemigo = 'BARRIDA'
    }
    // Opcional: Puedes agregar un alert aquí para ver qué eligió el enemigo y comprobar que funciona
    // alert("El enemigo atacó con: " + ataqueEnemigo)
}

// --- ESCUCHADORES DE EVENTOS (EVENT LISTENERS) ---

// Botón de seleccionar personaje
let botonPersonajeJugador = document.getElementById('boton-personaje');
botonPersonajeJugador.addEventListener('click', seleccionarPersonajeJugador);

// Botones de ataques físicos
let botonPunio = document.getElementById('boton-punio') 
botonPunio.addEventListener('click', ataquePunio)

let botonPatada = document.getElementById('boton-patada')
botonPatada.addEventListener('click', ataquePatada)

let botonBarrida = document.getElementById('boton-barrida')
botonBarrida.addEventListener('click', ataqueBarrida);