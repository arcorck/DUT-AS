import java.util.Comparator;

public class CompChaine2 implements Comparator<String>{
    public int compare(String s1, String s2){ // Attention : il faut que cette méthode soit public 
        if(s1.length() == s2.length()){
            return 0;
        }
        if(s1.length() > s2.length()){
            return -1;
        }
        return 1;
    }   
}