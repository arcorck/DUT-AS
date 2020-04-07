public class Wookie implements Personnage {
    private String nom, muniDe;
    private double taille;

    public Wookie(String nom, double taille, String muniDe) {
        this.nom = nom;
        this.muniDe = muniDe;
        this.taille = taille;
    }

    @Override
    public String toString() {
        return "Wookie{" +
                "nom='" + nom + '\'' +
                ", muniDe='" + muniDe + '\'' +
                ", taille=" + taille +
                '}';
    }

    @Override
    public String getRace() {
        return "Wookie";
    }

    @Override
    public double getTaille() {
        return taille;
    }

    @Override
    public String getCaracteristique() {
        return muniDe;
    }

    @Override
    public String getNom() {
        return nom;
    }
}
