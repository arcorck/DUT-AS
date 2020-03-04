public class Voiture {
    private int id, capacite;
    private String ville, nom;

    public Voiture (int id, java.lang.String v, int c){
        this.id = id;
        this.ville = v;
        this.capacite = c;
        this.nom = "";
    }

    public String getNom(){
        return this.nom;
    }

    public int getId(){
        return this.id;
    }

    public String getVille(){
        return this.ville;
    }

    public int getCapacite(){
        return this.capacite;
    }

}