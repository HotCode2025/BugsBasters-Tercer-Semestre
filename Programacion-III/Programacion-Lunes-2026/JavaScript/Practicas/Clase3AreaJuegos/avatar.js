function seleccionarPersonajeJugador() {

    let inputZuko = document.getElementById('zuko')
    let inputKatara = document.getElementById('katara')
    let inputAang = document.getElementById('aang')
    let inputToph = document.getElementById('toph')

    if (inputZuko.checked) {
        alert('Seleccionaste a ZUKO 🔥')
    } else if (inputKatara.checked) {
        alert('Seleccionaste a KATARA 💧')
    } else if (inputAang.checked) {
        alert('Seleccionaste a AANG 🌪️')
    } else if (inputToph.checked) {
        alert('Seleccionaste a TOPH 🌱')
    } else {
        alert('DEBES SELECCIONAR UN PERSONAJE')
    }
}

let botonPersonajeJugador = document.getElementById('boton-personaje');
botonPersonajeJugador.addEventListener('click', seleccionarPersonajeJugador);
