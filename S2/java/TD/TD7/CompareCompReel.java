import java.util.Comparator;

public class CompareCompReel implements Comparator<Complexe>{
    public int compare(Complexe a, Complexe b) { // Attention : il faut que cette méthode soit public 
        if(a.getReel() == b.getReel()){
            return 0;
        }
        if(a.getReel()>b.getReel()){
            return 1;
        }
        return -1;
    }  
     
}