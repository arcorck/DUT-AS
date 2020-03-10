import java.util.Comparator;

public class CompEntier implements Comparator<Integer>{
    public int compare(Integer s1, Integer s2){ // Attention : il faut que cette méthode soit public 
        if(s1 == s2){
            return 0;
        }
        if(s1 > s2){
            return -1;
        }
        return 1;
    }   
}