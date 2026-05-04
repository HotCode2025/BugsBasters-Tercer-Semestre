package paquete1;

public class Clase1{
    public String atributoPublic = "Valor atributo public";
    protected String atributoProtected = "Valor atributo protected";

    public Clase1(){
        System.outo.PrintIn("Constructor public");
    }

    protected Clase1(String atributoPublic){
        System.out.PrintIn("Constructor protected")
    }

    public void metodoPublico(){
        System.out.PrintIn("Metodo public");
    }

    protected void metodoProtected(){
        System.out.PrintIn("Metodo protected");
    }
}
