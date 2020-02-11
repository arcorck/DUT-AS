import java.util.*;
import java.lang.*;

public class MaxEtIndice {
   private int leMax;
   private int lIndice;

   public MaxEtIndice(int x, int y) {
      this.leMax = x;
      this.lIndice = y;
   }

   public int getMax(){
       return this.leMax;
   }

   public int getIndice(){
       return this.lIndice;
   }

   public String toString() {
     return "("+this.leMax + ", "+ this.lIndice+") ";
   }

   public static MaxEtIndice leMaxEtLIndice (List<Integer> maliste){
       int m = maliste.get(0);
       int ind = 0;
       for (int i = 1; i < maliste.size(); ++i){
           if (maliste.get(i) > m){
               m = maliste.get(i);
               ind = i;
           }
       }
       return new MaxEtIndice(m,ind);
   }

   public static HashMap<Integer, Integer> frequence(List<Integer> maliste){
        HashMap<Integer, Integer> res = new HashMap<>();
        for (Integer val : maliste){
            if (!res.containsKey(val)){
                res.put(val, 0);
            }
            res.put(val, res.get(val)+1);
        }
        return res;
    }

   public static void main (String[]args){
        List<Integer> l1 = new ArrayList<>();
        for (int i = 0; i < 20; ++i){
            l1.add(Math.round((float)Math.random()*100));
        }
        MaxEtIndice mi = MaxEtIndice.leMaxEtLIndice(l1);
        System.out.println("Dans la liste : " + l1 + "\nOn a " + mi);
        HashMap<Integer, Integer> dico = MaxEtIndice.frequence(l1);
        System.out.print(dico);
   }
}