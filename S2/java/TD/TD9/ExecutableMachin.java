import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class ListeVideException extends Exception{
// C'est tout (car Exception possède un constructeur sans paramètre) 
}

class BibMachin {
    public static int minimum(List<Integer> liste) throws ListeVideException { // minimum peut lever une exception (quand la lite est vide)
        if(liste.size() == 0){
            throw new ListeVideException(); // ici c'est le cas
        }else{
            return Collections.min(liste);
        } 
    }
}

public class ExecutableMachin{ 
    public static void main(String[] args) {
        List<Integer> a = new ArrayList<>();
        List<Integer> b = new ArrayList<>();
        a.add(1);
        a.add(2);
        try{
            System.out.println(BibMachin.minimum(a));
            System.out.println(BibMachin.minimum(b));
        }catch(ListeVideException e){
            System.out.println("Liste vide");
        }
    }
}