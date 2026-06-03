

function miFuncion(){
    console.log('Saludos desde mi funcion')
}
miFuncion();

let myFuncion = function (){
    console.log('Saludos desde la funcion anonima')
}

//Ahora vamos a crear una funcion flecha
let miFuncionFlecha = () => {
    console.log('Saludos desde mi funcion flecha');
}

//Hay mas variantes para la funcion flecha
miFuncionFlecha();

//Lo hacemos en una linea
const saludar = () => console.log('Saludo a todos desde esta funcion flecha')
console.log(saludar);


//Otro ejemplo
const saludar2 = () => {
    return 'Saludo a todos desde esta funcion flecha 2'
}

console.log(saludar2);

//Simplificamos la funcion anterior
const saludar3 = () => 'Saludos desde la funcion flecha tres'

console.log(saludar3);