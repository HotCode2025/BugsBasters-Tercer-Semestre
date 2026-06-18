'use strict';
// Veamos como evitar este error

try {
    Let x = 10 //Lo tramos con alt + flecha arriba o abajo
    //miFuncion(); //Capturamos el error de la función
    throw'Mi Error'; //Maneja tipo string
}
catch ( error ){ //Catchamos el error
    console.log( error );
}
finally {
    console.log('Termina la revisión de errores');
}

//La ejecución ahora continua...

console.log('Continuamos...'); //Esto no se llega a ver porque esta bloqueado

Let resultado = '';

try {
    //y = 5;
    if( isNaN(resultado)) throw 'No es un número';
    else if( resultado === '') throw 'Es cadena vacia';
    else if( resultado >= 0) throw 'Valor positivo';
    else if( resultado <= 0) throw 'Valor negativo';
}
catch(error) {
    console.log(error);
    console.log(error.name);
    console.log(error.message);
}
finally {
    console.log('Termina la revisión de errores 2');
}