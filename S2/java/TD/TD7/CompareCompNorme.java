import java.util.Comparator;
import java.lang.Math;

public class CompareCompNorme implements Comparator<Complexe>{
    public int compare(Complexe a, Complexe b) { // Attention : il faut que cette méthode soit public 
        if(Math.pow(a.getReel(), 2) + Math.pow(a.getImag(), 2) == Math.pow(b.getReel(), 2) + Math.pow(b.getImag(), 2) ){
            return 0;
        }
        if(Math.pow(a.getReel(), 2) + Math.pow(a.getImag(), 2) > Math.pow(b.getReel(), 2) + Math.pow(b.getImag(), 2)){
            return 1;
        }
        return -1;
    }  
     
}