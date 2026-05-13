(function() {
  // Creamos un elemento div para mostrar el reloj
  const relojDiv = document.createElement('div');
  relojDiv.id = 'reloj';
  relojDiv.style.fontSize = '48px';
  relojDiv.style.fontFamily = 'Arial, sans-serif';
  relojDiv.style.fontWeight = 'bold';
  relojDiv.style.position = 'fixed';
  relojDiv.style.top = '20px';
  relojDiv.style.right = '20px';
  relojDiv.style.padding = '10px';
  relojDiv.style.borderRadius = '8px';
  relojDiv.style.zIndex = '9999';
  document.body.appendChild(relojDiv);

  // aqui usamos una función para actualizar el reloj y el color según el día
  function actualizarReloj() {
    const ahora = new Date();

    // obtenemos horas, minutos y segundos
    let horas = ahora.getHours();
    let minutos = ahora.getMinutes();
    let segundos = ahora.getSeconds();

    // aqui formateamos con ceros a la izquierda si es menor a 10
    horas = horas < 10 ? '0' + horas : horas;
    minutos = minutos < 10 ? '0' + minutos : minutos;
    segundos = segundos < 10 ? '0' + segundos : segundos;

    // mostramos la hora en formato HH:MM:SS
    const horaFormateada = `${horas}:${minutos}:${segundos}`;
    relojDiv.textContent = horaFormateada;

    // cambiamos color según el día de la semana (0=domingo, 1=lunes, ..., 6=sábado)
    const dia = ahora.getDay();
    let color;

    switch(dia) {
      case 0: color = '#FF4500'; break; // Domingo - rojo anaranjado
      case 1: color = '#1E90FF'; break; // Lunes - azul
      case 2: color = '#32CD32'; break; // Martes - verde
      case 3: color = '#FFD700'; break; // Miércoles - amarillo
      case 4: color = '#FF69B4'; break; // Jueves - rosa
      case 5: color = '#8A2BE2'; break; // Viernes - azul violeta
      case 6: color = '#FF8C00'; break; // Sábado - naranja oscuro
      default: color = '#000000'; // Negro por defecto
    }

    relojDiv.style.color = color;
  }

  // Actualizar el reloj inmediatamente y luego cada segundo
  actualizarReloj();
  setInterval(actualizarReloj, 1000);
})();