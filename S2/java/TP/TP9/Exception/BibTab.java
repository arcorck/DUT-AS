import java.util.ArrayList;
import java.util.Collections;

public class BibTab {
    public static int plusPetitPlusGrand(ArrayList<Integer> tab, int nb) throws PasDeTelElementException, PasdeMaxException{
        if (!tab.contains(nb)){
            throw new PasDeTelElementException();
        }
        if (nb == Collections.max(tab)){
            throw new PasdeMaxException();
        }
        int plusplus = Collections.max(tab);
        for (Integer i : tab){
            if (i > nb && i < plusplus){
                plusplus = i;
            }
        }
        return plusplus;
    }
}
