import java.util.Collections;
import java.util.NoSuchElementException;

public class ExecTab {

    public static void main(String[] args) {
        Tableau t = new Tableau();
        t.remplir();
        Tableau t1 = new Tableau();
        try{
            System.out.print("min de t : ");
            System.out.println(Collections.min(t.getTableau()));
        }catch(NoSuchElementException m){
            System.out.println("Il n’y a pas de minimum : le tableau est vide !");
        }
        try{
            System.out.print("min de t1 : ");
            System.out.println(Collections.min(t1.getTableau()));
        }catch(NoSuchElementException m){
            System.out.println("Il n’y a pas de minimum : le tableau est vide !");
        }
        try{
            System.out.print("max de t : ");
            System.out.println(t.getMax());
        }catch(NoSuchElementException m){
            System.out.println("Il n’y a pas de maximum : le tableau est vide !");
        }
        try{
            System.out.print("max de t1 : ");
            System.out.println(t1.getMax());
        }catch(NoSuchElementException m){
            System.out.println("Il n’y a pas de maximum : le tableau est vide !");
        }
        try{
            System.out.print("min2 de t : ");
            System.out.println(t.getMin());
        }catch(PasDeTelElementException m){
            System.out.println("Il n’y a pas de minimum : le tableau est vide !");
        }
        try{
            System.out.print("min2 de t1 : ");
            System.out.println(t1.getMin());
        }catch(PasDeTelElementException m){
            System.out.println("Il n’y a pas de minimum : le tableau est vide : " + m.toString());
        }
        try{
            System.out.print("t[3] : ");
            System.out.println(t.getElement(3));
        }catch(NoSuchElementException m){
            System.out.println("Indice non valable");
        }
        try{
            System.out.print("t1[3] : ");
            System.out.println(t1.getElement(3));
        }catch(NoSuchElementException m){
            System.out.println("Indice non valable");
        }
    }
}
