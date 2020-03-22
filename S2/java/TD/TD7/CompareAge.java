import java.util.Comparator;

public class CompareAge implements Comparator<Integer>{
    public int compare(Integer a, Integer b) { // Attention : il faut que cette méthode soit public 
        if(a == b){
            return 0;
        }
        if(a>b){
            return 1;
        }
        return -1;
    }   
}