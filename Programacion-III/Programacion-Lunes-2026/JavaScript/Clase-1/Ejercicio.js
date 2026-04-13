// 1. Clase Padre: DispositivoEntrada
// Esta es la clase base (superclase) que será heredada por otros dispositivos de entrada como Ratón y Teclado.
// Contiene las propiedades comunes que todos los dispositivos de entrada comparten.
class DispositivoEntrada {
    // El constructor inicializa las propiedades de la clase cuando se crea un nuevo objeto
    constructor(tipoEntrada, marca) {
        this._tipoEntrada = tipoEntrada; // Tipo de conexión (por ejemplo: USB, Bluetooth)
        this._marca = marca;             // Marca del dispositivo (por ejemplo: HP, Logitech)
    }

    // Métodos Getters y Setters: Permiten obtener y modificar de forma controlada los valores de las propiedades privadas (con guion bajo _)
    get tipoEntrada() { return this._tipoEntrada; }
    set tipoEntrada(tipoEntrada) { this._tipoEntrada = tipoEntrada; }

    get marca() { return this._marca; }
    set marca(marca) { this._marca = marca; }
}

// 2. Clase Hija: Raton
// La palabra clave 'extends' indica que Raton hereda las propiedades y métodos de DispositivoEntrada
class Raton extends DispositivoEntrada {
    // Variable estática: Pertenece a la clase en sí y no a cada objeto individual. Sirve para llevar la cuenta de cuántos ratones se han creado.
    static contadorRatones = 0;

    constructor(tipoEntrada, marca) {
        // 'super' llama al constructor de la clase padre (DispositivoEntrada) pasándole los valores que necesita
        super(tipoEntrada, marca);
        // Cada vez que se crea un nuevo objeto Raton, aumentamos el contador y le asignamos ese número como su ID único
        this._idRaton = ++Raton.contadorRatones;
    }

    // Solo tenemos un getter para el ID porque no queremos que se pueda modificar una vez creado
    get idRaton() { return this._idRaton; }

    // Sobrescribimos el método toString para que devuelva una cadena de texto con la información específica del ratón
    toString() {
        return `[Ratón: ID ${this._idRaton}, Tipo: ${this._tipoEntrada}, Marca: ${this._marca}]`;
    }
}

// 3. Clase Hija: Teclado
// Funciona exactamente igual que la clase Raton, heredando de DispositivoEntrada
class Teclado extends DispositivoEntrada {
    static contadorTeclados = 0; // Contador exclusivo para teclados

    constructor(tipoEntrada, marca) {
        super(tipoEntrada, marca); // Llama al constructor de DispositivoEntrada
        this._idTeclado = ++Teclado.contadorTeclados; // Asigna un ID único y secuencial al teclado
    }

    get idTeclado() { return this._idTeclado; }

    toString() {
        return `[Teclado: ID ${this._idTeclado}, Tipo: ${this._tipoEntrada}, Marca: ${this._marca}]`;
    }
}

// 4. Clase Independiente: Monitor
// Esta clase no hereda de DispositivoEntrada (ya que el monitor es de salida), por lo que es una clase base propia.
class Monitor {
    static contadorMonitores = 0;

    constructor(marca, tamanio) {
        // Al igual que antes, asignamos un ID único autoincremental
        this._idMonitor = ++Monitor.contadorMonitores;
        this._marca = marca;        // Marca del monitor (ej. Dell, Samsung)
        this._tamanio = tamanio;    // Tamaño de la pantalla en pulgadas (ej. 24, 27)
    }

    get idMonitor() { return this._idMonitor; }

    get marca() { return this._marca; }
    set marca(marca) { this._marca = marca; }

    get tamanio() { return this._tamanio; }
    set tamanio(tamanio) { this._tamanio = tamanio; }

    toString() {
        return `[Monitor: ID ${this._idMonitor}, Marca: ${this._marca}, Tamaño: ${this._tamanio}"]`;
    }
}

// 5. Clase Compuesta: Computadora
// Esta clase utiliza "Composición", es decir, agrupa objetos de otras clases (Monitor, Teclado, Raton) para formar algo más grande.
class Computadora {
    static contadorComputadoras = 0;

    // El constructor recibe instancias (objetos) de Monitor, Teclado y Raton, además del nombre de la PC
    constructor(nombre, monitor, teclado, raton) {
        this._idComputadora = ++Computadora.contadorComputadoras;
        this._nombre = nombre;
        this._monitor = monitor; // Guarda el objeto monitor entero
        this._teclado = teclado; // Guarda el objeto teclado entero
        this._raton = raton;     // Guarda el objeto raton entero
    }

    get idComputadora() { return this._idComputadora; }

    // Al imprimir la computadora usando "toString", JavaScript llamará automáticamente al método "toString" de cada uno de los componentes (monitor, teclado, raton)
    toString() {
        return `Computadora ${this._idComputadora}: ${this._nombre} \n   ${this._monitor} \n   ${this._teclado} \n   ${this._raton}`;
    }
}

// 6. Clase Agrupadora: Orden
// Esta clase sirve para simular la compra de una o más computadoras
class Orden {
    static contadorOrdenes = 0;

    constructor() {
        this._idOrden = ++Orden.contadorOrdenes;
        this._computadoras = []; // Inicializamos un arreglo (array) vacío donde guardaremos las computadoras de esta orden
    }

    get idOrden() { return this._idOrden; }

    // Este método toma un objeto computadora pasado por parámetro y lo añade al arreglo usando .push()
    agregarComputadora(computadora) {
        this._computadoras.push(computadora);
    }

    // Este método recorre (con un bucle for-of) todas las computadoras en el arreglo y concatena su información en la variable 'computadorasOrden'
    mostrarOrden() {
        let computadorasOrden = '';
        for (let computadora of this._computadoras) {
            computadorasOrden += `\n ${computadora}`;
        }
        console.log(`Orden: ${this._idOrden}, Computadoras: ${computadorasOrden}`);
    }
}

// ==========================================
// ZONA DE PRUEBAS (Testing)
// ==========================================

console.log('--- Creando Periféricos ---');
// 1. Instanciamos los diferentes componentes por separado brindándoles sus características correspondientes
let raton1 = new Raton('USB', 'HP');
let raton2 = new Raton('Bluetooth', 'Logitech');
let teclado1 = new Teclado('Bluetooth', 'Logitech');
let teclado2 = new Teclado('USB', 'Corsair');
let monitor1 = new Monitor('Dell', 27);
let monitor2 = new Monitor('Samsung', 24);

// Verificamos por consola que los objetos se hayan creado correctamente
console.log(raton1.toString());
console.log(teclado1.toString());
console.log(monitor1.toString());

console.log('\n--- Armando Computadoras ---');
// 2. Pasamos los objetos creados anteriormente para construir objetos Computadora
let computadora1 = new Computadora('PC Diseño', monitor1, teclado1, raton1);
let computadora2 = new Computadora('PC Gaming', monitor2, teclado2, raton2);
console.log(computadora1.toString());

console.log('\n--- Generando Órdenes ---');
// 3. Creamos órdenes y usamos el método agregarComputadora para meter las PC en la orden
let orden1 = new Orden();
orden1.agregarComputadora(computadora1);
orden1.agregarComputadora(computadora2);
orden1.mostrarOrden(); // Esto imprimirá toda la info de la orden y sus computadoras

// Creamos otra orden independiente para demostrar el autoincremento de IDs
let orden2 = new Orden();
// Esta computadora reutiliza el monitor2, el teclado1 y el raton2 creados previamente
let computadora3 = new Computadora('PC Oficina', monitor2, teclado1, raton2);
orden2.agregarComputadora(computadora3);
orden2.mostrarOrden();