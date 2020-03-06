import java.util.ArrayList;
import java.util.List;

public class Covoiturage{
    private ArrayList<Personne> personnes;
    private ArrayList<Voiture> voitures;

    public Covoiturage(ArrayList<Voiture> v, ArrayList<Personne> p){
        this.voitures = v;
        this.personnes = p;
    }

    public boolean villeDesservie(String ville){
        for (Voiture v : this.voitures){
            if (v.getVille().equals(ville)){
                return true;
            }
        }
        return false;
    }

    public int nbPersonnes(String v){
        int res = 0;
        for (Personne p : this.personnes){
            if (p.getVille().equals(v)){
                res++;
            }
        }
        return res;
    }

    public int getIdentifiant(String nomPersonne){
        for (Personne p : this.personnes){
            if (p.getNom().equals(nomPersonne)){
                return p.getId();
            }
        }
        return -1;
    }

    public boolean capaciteSuffisante (String ville){
        int nbhabville = 0;
        for (Personne p : this.personnes){
            if (p.getVille() == ville){
                nbhabville++;
            }
        }
        int nbplace = 0;
        for (Voiture v : this.voitures){
            if (v.getVille() == ville){
                nbplace+=v.getCapacite();
            }
        }
        return nbhabville <= nbplace; //Car il y a 5 places dans chaque voiture
    }

    public boolean villeEstDans (ArrayList<String> villes, String ville){
        for (String v : villes){
            if (v.equals(ville)){
                return true;
            }
        }
        return false;
    }

    public ArrayList<String> getVilles(){
        ArrayList<String> res = new ArrayList<>();
        for (Personne p : this.personnes){
            if (! villeEstDans(res, p.getVille())){
                res.add(p.getVille());
            }
        }
        for (Voiture v : this.voitures){
            if (! villeEstDans(res, v.getVille())){
                res.add(v.getVille());
            }
        }
        return res;
    }

    public boolean capaciteSuffisante(){
        ArrayList<String> lesvilles = this.getVilles();
        for (String v : lesvilles){
            if (! capaciteSuffisante(v)){
                return false;
            }
        }
        return true;
    }

    //methode renvoyant le nombre de personnes d'une ville 
    public int nbPersVille (String ville){
        int nbpers = 0;
        for (Personne p : this.personnes){
            if (p.getVille() == ville){
                nbpers++;
            }
        }
        return nbpers;
    }

    //methode renvoyant le nombre de conducteurs d'une ville 
    public int nbConductVille (String ville){
        int nbcond = 0;
        for (Personne p : this.personnes){
            if (p.getVille() == ville && p.peutConduire()){
                nbcond++;
            }
        }
        return nbcond;
    }

    //methode qui renvoie la plus grande capacite existante d'une voiture
    public int capaciteMaxVoiture (){
        int cap = 0;
        for (Voiture v : this.voitures){
            if (v.getCapacite() > cap){
                cap = v.getCapacite();
            }
        }
        return cap;
    }

    //methode qui renvoie pour une ville le nombre de voitures avec une capacite donnee dans une ville donnee
    public int nbvoitcap (int cap, String ville){
        int nbvoit = 0;
        for (Voiture v : this.voitures){
            if (v.getCapacite() == cap && v.getVille() == ville){
                nbvoit++;
            }
        }
        return nbvoit;
    }

    //methode qui renvoie pour une ville le nombre de voiture necessaires
    public int nbVoitures (String ville){
        int nbvoitures = 0;
        int nbvoyageurs = nbPersVille(ville);
        int capmax = capaciteMaxVoiture();
        while (nbvoyageurs > 0 && capmax > 0){
            nbvoitures += nbvoitcap(capmax, ville);
            nbvoyageurs = nbvoyageurs - (capmax * nbvoitcap(capmax, ville));
            capmax --;
        }
        return nbvoitures;
    }

    public boolean estPossible(){
        if (this.capaciteSuffisante()){
            ArrayList<String> lesvilles = this.getVilles();
            for (String v : lesvilles){
                if (this.nbConductVille(v) < this.nbVoitures(v)){
                    return false;
                }
            }
            return true;
        }else{
            return false;
        }
    }

   /* public int[] attribution (){
        
    }*/
    
    //retourne la premiere la premiere personne de la liste dans l'ordre alphabétique et la supprime de la liste 
    public Personne premiere_personne_alpha (){
        Personne min = this.personnes.get(0);
        int indice;
        indice = 0;
        for (int i = 1; i < this.personnes.size(); i++){
            if (this.personnes.get(i).getNom().compareTo(min.getNom()) < 0){
                min = this.personnes.get(i);
                indice = i;
            }
        }
        this.personnes.remove(indice);
        return min;
    }

    //trie la liste des personnes
    public void triePersonnes (){
        ArrayList<Personne> res = new ArrayList<>();
        while (! this.personnes.isEmpty()){
            res.add(this.premiere_personne_alpha());
        }
        this.personnes = res;
    }

    public int getIdentifiantDicho (String nomp) {
        int deb = 0;
        int fin = this.personnes.size()-1;
        int milieu;
        while (deb <= fin){
            milieu = (deb + fin)/2;
            if (nomp.compareTo(this.personnes.get(milieu).getNom()) == 0){
                return this.personnes.get(milieu).getId();
            }else{
                if (nomp.compareTo(this.personnes.get(milieu).getNom()) < 0){
                    fin = milieu-1;
                }else{
                    deb = milieu+1;
                }
            }
        }
        return -1;
    }
}