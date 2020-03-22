import java.util.ArrayList;

public class LibEntiers{

    public static boolean recherche (ArrayList<Integer> liste, Integer elem){
        int bas = 0;
        int haut = liste.size()-1;
        int milieu = 0;
        while (bas < haut){
            milieu = (bas+haut)/2;
            if (liste.get(milieu) < elem){
                bas = milieu + 1;
            }else{
                haut = milieu;
            }
        }
        return bas < liste.size() && elem == liste.get(bas);
    }

    public static boolean rechercheDecroissant (ArrayList<Integer> liste, Integer elem){
        int bas = liste.size()-1;
        int haut = 0;
        int milieu = 0;
        while (haut < bas){
            milieu = (bas+haut)/2;
            if (liste.get(milieu) < elem){
                haut = milieu + 1;
            }else{
                bas = milieu;
            }
        }
        return haut < liste.size() && elem == liste.get(haut);
    }

}