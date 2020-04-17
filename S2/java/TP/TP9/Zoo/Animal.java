public class Animal {
    private String nom;
    private boolean blesse;

    public Animal(String nom, boolean blesse) {
        this.nom = nom;
        this.blesse = blesse;
    }

    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public boolean isBlesse() {
        return blesse;
    }

    public void setBlesse(boolean blesse) {
        this.blesse = blesse;
    }
    
    public String toString(){
        if (blesse){
            return "Le " + nom + " est bléssé\n";
        }else{
            return "Le " + nom + " n'est pas bléssé\n";
        }
    }
}
