import java.util.Comparator;

public class CompareTaille implements Comparator<Personnage>{
    public int compare(Personnage a, Personnage b) { // Attention : il faut que cette méthode soit public
        if(a.getTaille() == b.getTaille()){
            return 0;
        }
        if(a.getTaille()>b.getTaille()){
            return 1;
        }
        return -1;
    }

}