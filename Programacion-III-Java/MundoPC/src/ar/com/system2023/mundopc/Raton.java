package ar.com.system2023.mundopc;

/**
 *
 * @author brian
 */
public class Raton extends DispositivoEntrada {
    private final int idRaton;
    private static int contadorRatones;
    
    // La "R" debe ser mayúscula para que sea un constructor válido
    public Raton(String tipoEntrada, String marca) {
        super(tipoEntrada, marca);
        this.idRaton = ++Raton.contadorRatones;
    }

    @Override
    public String toString() {
        // Se agregó el "+" antes de '}'
        return "Raton{" + "idRaton=" + idRaton + ", " + super.toString() + '}';
    }
}