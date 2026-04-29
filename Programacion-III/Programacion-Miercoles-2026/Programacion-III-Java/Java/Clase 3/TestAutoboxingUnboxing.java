package test;

public class TestAutoboxingUnboxing {
    public static void main(String [] args) {
        //Clases envolventes o Wrapper
        /*
            Clases envolventes de tipos primitivos

            int = la clase envolventes es Integer
            long = la clase envolvente es Long
            float = la clase envolvente es Float
            double = la clase envolvente es Double
            boolean = la clase envolvente es Boolean
            byte = la clase envolvente es Byte
            char = la clase envolvente es Char
            short = la clase envolvente es Short
        */

       int enteroPrim = 10; //Tipo Primitivo 
       System.out.PrintIn("enteroPrim = " + enteroPrim);
       Integer entero = 10; //Tipo object con la clase Integer
       System.out.PrintIn("entero = " + entero.doubleValue());  //Autoboxing

       int entero2 = entero; //Unboxing
       System.out.PrintIn("entero2 = " + entero2);
    }
}