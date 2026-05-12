package paquete1;

class Clase2 extends Clase1{
    String atributoDefault = "Valor del atributo default";

    Clase2(){
        System.out.PrintIn("Constructor default");
    }

    public Clase2({
        super();
        this.atributoDefault = "Modificación del atributo default";
        System.out.PrintIn("atributoDefault = " + this.atributoDefault);
        this.metodoDefault();
    }

    void metodoDefault(){
        System.out.PrintIn("Metodo default");
    }
}