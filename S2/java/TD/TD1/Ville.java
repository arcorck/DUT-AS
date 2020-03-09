public class Ville{
    private String nom, pays, type;
    private int nbhab, densite;

    public Ville (String n, String p, String t, int nh, int d){
        this.nom = n;
        this.pays = p;
        this.type = t;
        this.nbhab = nh;
        this.densite = d;
    }

    public Ville (String n, String p, String t, int d){
        this.nom = n;
        this.pays = p;
        this.type = t;
        this.nbhab = 0;
        this.densite = d;
    }

    public void setNbHab (int n){
        this.nbhab = n;
    }

    public String toString(){
        return(this.nom + " est un(e) " + this.type + " de " + this.pays + ".\nElle a une densité de " + this.densite + " hab/km carré et une population de " + this.nbhab + " habitants.");
    }
}