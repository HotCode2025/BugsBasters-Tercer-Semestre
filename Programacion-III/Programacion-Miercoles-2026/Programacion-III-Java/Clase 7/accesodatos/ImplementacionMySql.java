package accesodatos;

public class ImplementacionMySql implements IAccesoDatos{
   @Override
    public void insertar() {
        System.out.println("Insertar en MySQL");
    } 

    @Override
    public void listar() {
        System.out.println("Listar en MySQL");
    }

    @Override
    public void actualizar() {
        System.out.println("Actualizar en MySQL");
    }   

    @Override
    public void eliminar() {
        System.out.println("Eliminar en MySQL");
    }
}