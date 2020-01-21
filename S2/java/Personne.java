public class Personne{
    private String nom;
	private String prenom;
    private int journaissance;
    private int moisnaissance;
    private int anneenaissance;
    private double taille;

    public Personne (String nom, String prenom, int jour, int mois, int annee, double taille){
        this.nom = nom;
        this.prenom = prenom;
        this.journaissance = jour;
        this.moisnaissance = mois;
        this.anneenaissance = annee;
        this.taille = taille;
    }

    public void setAnneeNaissance (int a){
        this.anneenaissance = a;
    }

    public String signeAstrologique (){
        return ("flemme de l'écrire, on verra plus tard");
    }

    public String getNom (){
        return this.nom;
    }

    public String getPrenom (){
        return this.prenom;
    }

    public int getAnneeNaissance (){
        return this.anneenaissance;
    }

    public double getTaille (){
        return this.taille;
    }

    public void setTaille(double t){
        this.taille = t;
    }

    public String toString(){
        return (this.prenom + " " + this.nom + " est né le " + this.journaissance + "/" + this.moisnaissance + "/" + this.anneenaissance + " et mesure " + this.taille + "m");
    }
}