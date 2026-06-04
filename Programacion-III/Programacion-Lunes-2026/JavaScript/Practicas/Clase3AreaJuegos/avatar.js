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

let botonPersonajeJugador = document.getElementById('boton-personaje');
botonPersonajeJugador.addEventListener('click', seleccionarPersonajeJugador);