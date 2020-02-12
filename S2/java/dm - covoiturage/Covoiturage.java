import java.util.ArrayList;

public class Covoiturage{
    private ArrayList<Personne> personnes;
    private ArrayList<Voiture> voitures;

    public Covoiturage(ArrayList<Personne> p, ArrayList<Voiture> v){
        this.personnes = p;
        this.voitures = v;
    }

    public boolean villeDesservie(String v){
        for (Personne p : this.personnes){
            if (p.getVille().equals(v)){
                return true;
            }
        }
        return false;
    }
    
    public int nbPersonnes(String v){
        return this.personnes.size();
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
            if (v == ville){
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

    public boolean capaciteSuffisante2(){
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

    //methode qui renvoie la plus grande capacite existante
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
        if (this.capaciteSuffisante2()){
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

    public int[] attribution (){
        
    }
}