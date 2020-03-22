import java.util.Comparator;

public class BibCollections{
    public static boolean pluspetit (Complexe [] tab, Comparator<Complexe> c, Complexe a){
        for (int i = 0; i < tab.length ; i++){
            if (c.compare(a, tab[i]) > 0){
                return false;
            }
        }
        return true;
    }

    public static boolean entredeux (Complexe [] tab, Comparator<Complexe> c, Complexe a, Complexe b){
        for (int i = 0; i < tab.length ; i++){
            if (c.compare(a, tab[i]) > 0 || c.compare(b, tab[i]) < 0){
                return false;
            }
        }
        return true;
    }

    static public String affTab (Complexe [] tab){
        String res = "";
        for (int i = 0; i < tab.length; i++){
            res += tab[i].toString();
        }
        return res;
    }

    public static void main(String[] args) {
        Complexe [] tab = new Complexe [5];
        tab[0] = new Complexe(56.3, -2.5);
        tab[1] = new Complexe(-67.9, 0.0);
        tab[2] = new Complexe(-21.6, -38.0);
        tab[3] = new Complexe(98.09, 87.543);
        tab[4] = new Complexe(-92.87, 65.67);
        System.out.println(affTab(tab));
        System.out.println(pluspetit(tab, new CompareCompNorme(), new Complexe(0, 0)));
        System.out.println(pluspetit(tab, new CompareCompNorme(), new Complexe(100.0, 100.0)));
        System.out.println(pluspetit(tab, new CompareCompReel(), new Complexe(-100.0, -100.0)));
        System.out.println(pluspetit(tab, new CompareCompReel(), new Complexe(100.0, 100.0)));
        System.out.println(entredeux(tab, new CompareCompReel(), new Complexe(-100.0, -100.0),  new Complexe(100.0, 100.0)));
        System.out.println(entredeux(tab, new CompareCompReel(), new Complexe(-50.0, -100.0),  new Complexe(50.0, 100.0)));
    }
}