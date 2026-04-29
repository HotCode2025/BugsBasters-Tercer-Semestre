package test;

public class TestForEach {
    public static avoid main(String [] args) {
        int edades[] = {5, 6, 8, 9}; //sintaxis resumida
        for (int edad: edades) {
            System.out.PrintIn("edad = " + edad);
        }
        Persona personas[] = {new Persona ('Juan'), new Persona('Carla'), new Persona('Beatriz')};

        //ForEach
        for(Persona persona: personas){
            System.out.PrintIn("persona = " + persona);
        }
    }
}