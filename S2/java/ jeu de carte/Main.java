import java.util.List;
import java.util.ArrayList;
import java.lang.Math;

public class Main{
    private List<Carte> main;
    private Carte selectionnee;

    public Main (){
        this.main = new ArrayList<>();
        this.selectionnee = null;
    }

    public void add (Carte c){
        this.main.add(c);
    }

    public Carte getCarteSelectionnee() {
        return this.selectionnee;
    }

    public List<Carte> getMesCartes(){
        return this.main;
    }

    public void jouer (){
        this.main.remove(this.selectionnee);
    }
    
    public void jouerToutesCouleurs(){
        for (Carte c : this.main){
            if (c.getCouleur().equals(this.selectionnee.getCouleur())){
                this.main.remove(c);
            }
        }
        this.selectionnee = null;
    }

    public void jouerToutesValeurs(){
        for (Carte c : this.main){
            if (c.getValeur().equals(this.selectionnee.getValeur())){
                this.main.remove(c);
            }
        }
        this.selectionnee = null;
    }

    public void piocher (){
        int nombreAleatoire = 1 + (int)(Math.random() * ((10 - 1) + 1));
        List<String> couleurs = new ArrayList<>();
        couleurs.add("trefle");
        couleurs.add("carreau");
        couleurs.add("coeur");
        couleurs.add("pique");
        int couleurAleatoire = 1 + (int)(Math.random() * ((4 - 1) + 1));
        Carte c = new Carte(nombreAleatoire, couleurs.get(couleurAleatoire));
        this.main.add(c);
    }

    public void setCarteSelectionee(Carte c){
        this.selectionnee = c;
    }

    public Carte minVal (){
        int min = this.main.get(0).getValeurInt();
        Carte res = null;
        for (Carte c : this.main){
            if (c.getValeurInt() < min){
                min = c.getValeurInt();
                res = c;
            }
        }
        return res;
    }

    public void triParValeurs(){
        List<Carte> tmp = new ArrayList<>(this.main);
        List<Carte> res = new ArrayList<>();
        while (!tmp.isEmpty()){
            res.add(minVal());
            tmp.remove(minVal());
        }
        this.main = res;
    }

    public void supprimerCouleur (String couleur, List<Carte> l){
        for (Carte c : this.main){
            if (c.getCouleur().equals(couleur)){
                l.add(c);
            }
        }
    }

    public void triParCouleurs(){
        List<Carte> res = new ArrayList<>();
        supprimerCouleur("trefle", res);
        supprimerCouleur("carreau", res);
        supprimerCouleur("coeur", res);
        supprimerCouleur("pique", res);
        this.main = res;
    }
}