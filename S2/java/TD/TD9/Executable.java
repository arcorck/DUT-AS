import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.NoSuchElementException;

public class Executable {
    
    public static void afficheMin(List<Integer> liste){
        System.out.println("Ma liste: " + liste);
        try{
            Integer minimum = Collections.min(liste); 
            System.out.println("Et voici le minimum:"); 
            System.out.println(minimum);
        }catch (Exception m){
            System.out.println("La liste est vide");
        }
    }

    public static void afficheMin2(List<Integer> liste) throws NoSuchElementException{
        System.out.println("Ma liste: " + liste);
        if (liste.isEmpty()){
            throw new NoSuchElementException();
        }else{
            Integer minimum = Collections.min(liste); 
            System.out.println("Et voici le minimum:"); 
            System.out.println(minimum);
        }
    }
    public static void main(String[] args) {
        List<Integer> liste = new ArrayList<>(); 
        System.out.println("Liste 1"); 
        afficheMin(liste); 
        try {
            afficheMin2(liste);
        }catch(NoSuchElementException e){
            System.out.println("La liste est vide");
        }
        System.out.println("Liste 2"); 
        List<Integer> liste2 = new ArrayList<>(); 
        liste2.add(1);
        liste2.add(7); 
        liste2.add(-2); 
        afficheMin(liste2);
        try {
            afficheMin2(liste2);
        }catch(NoSuchElementException e){
            System.out.println("La liste est vide");
        }
    } 
}