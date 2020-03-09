import java.lang.Math;
import java.util.*;

public class Plateau{
    private List<Float> plateau;

    Plateau (int taille){
        this.plateau = new ArrayList<>(taille);
        for (int i = 0; i < taille; i++){
            plateau.set(i, (float)Math.random()*100);
        }
    }

    public String toString(){
        String res = "";
        for (Float n : this.plateau){
            res += n;
            res += " ; "; 
        }
        return res;
    }

    public static void main (String[]args){
        Plateau p = new Plateau(6);
        System.out.println(p);
    }
}