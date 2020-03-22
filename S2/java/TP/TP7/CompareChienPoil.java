import java.util.Comparator;

public class CompareChienPoil implements Comparator<Chien>{
    public int compare(Chien a, Chien b) { // Attention : il faut que cette méthode soit public 
        if(a.getLongueur() == b.getLongueur()){
            return 0;
        }
        if(a.getLongueur()>b.getLongueur()){
            return 1;
        }
        return -1;
    }  
     
}