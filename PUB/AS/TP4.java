import java.util.List;
import java.util.Collections;
import java.util.ArrayList;
import java.util.Map;
import java.util.Set;
import java.util.HashSet;
import java.util.HashMap;
import java.lang.Math;

// classe permettant de fournir la valeur et l'indice
class MaxEtIndice{
    private int leMax;
    private int lIndice;
    public MaxEtIndice(int x, int y){
        this.leMax=x;
        this.lIndice=y;
    }
    public String toString(){
        return " valeur max = "+this.leMax+" a l'indice : " + this.lIndice;
    }
    
    public static MaxEtIndice leMaxEtLIndice(List<Integer> maliste){
        
        return new MaxEtIndice(m, ind);
    }
    
    public static void main(String [] arg){
        List<Integer> l1 = new ArrayList<>();
        for(int i = 0; i < 20; ++i){
	        l1.add(Math.round((float)Math.random()*100));
        }
        
    }
}

