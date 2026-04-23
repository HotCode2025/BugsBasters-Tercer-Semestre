class Empleado {
    constructor(nombre, sueldo){
this._nombre = nombre;
this._sueldo = sueldo;
    }

    obtenerDetalles(){
        return `Empleado: Nombre: ${this._nombre}, Sueldo: ${this._sueldo}`;
    }        
}


class Gerente extends Empleado {
    constructor(nombre, sueldo, departamento){
        super(nombre, sueldo);
        this._departamento = departamento;
    }

    //Agregamos la sobreescritura
    obtenerDetalles(){
        return `Gerente ${super.obtenerDetalles()}, Departamento: ${this._departamento}`;
    }

let gerente1 = new Gerente("Juan", 5000, "Ventas");
console.log(gerente1.obtenerDetalles()); //obeto de la clase hija

let empleado1 = new Empleado("Maria", 3000);
console.log(empleado1.obtenerDetalles()); //objeto de la clase padre