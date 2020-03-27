import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;

public class BibCollections {
    public static List<Integer> intersection (List<Integer> L1, List<Integer> L2){
        int i1 = 0;
        int i2 = 0;
        List<Integer> listeARendre = new ArrayList<>();
        while(i1<L1.size() && i2<L2.size()){
          if (L1.get(i1)<L2.get(i2)){
            ++i1;
          }else if (L1.get(i1)>L2.get(i2)){
            ++i2;
          }else{
            listeARendre.add(L1.get(i1));
            ++i1;
            ++i2;
          }
        }
        return listeARendre;
      }

      public static List<Integer> intersection(List<Integer> liste1, List<Integer> liste2,  List<Integer> liste3) {
        List<Integer> aux = intersection(liste1, liste2);
        List<Integer> res = intersection(aux, liste3);
        return res;
      } 


    public static int elementMajoritaire (List<Integer> liste){
        Map<Integer, Integer> freq = new HashMap<>();
        for(Integer elt : liste){
            if(!freq.containsKey(elt)){
                freq.put(elt, 1);
            }
            else{
                freq.put(elt, freq.get(elt)+1);
            }
        }
        Integer maxElt=liste.get(0);
        for(Integer elt : freq.keySet()){
            if(freq.get(elt)>freq.get(maxElt)){
                maxElt=elt;
            }
        }
      
        return maxElt;
    }
}