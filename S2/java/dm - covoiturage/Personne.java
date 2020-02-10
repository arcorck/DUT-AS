public class Personne {
    private int id;
    private String ville, nom;
    private boolean permis;

    public Personne(int id, String nom, String ville, boolean permis){
        this.id = id;
        this.nom = nom;
        this.permis = permis;
        this.ville = ville;
    }

    public String getNom(){
        return this.nom;
    }

    public String getVille(){
        return this.ville;
    }

    public int getId(){
        return this.id;
    }

    public boolean peutConduire(){
        return this.permis;
    }
}