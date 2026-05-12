package paquete2;

public class Clase4 {
    private String atributoPrivate = "atributo privado";

    private Clase4(){
        System.out.printIn("Constructor privado");
    }

    //Creamos un constructor public para poder crear objetos
    public Clase4 (String argumento){ //Aqui se puede llamar al constructor vacio
        this();
        System.out.printIn("Constructor publico");

    }

    //Metodo private
    private void metodoPrivado(){
        System.out.printIn("Método privado");
    }

    public String getAtributoPrivate(){
        return atributoPrivate;
    }

    public void setAtributoPrivate(String atributoPrivate) {
        this.atributoPrivate = atributoPrivate;
    }
}