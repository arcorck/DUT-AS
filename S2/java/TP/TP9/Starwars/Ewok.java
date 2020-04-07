public class Ewok implements Personnage {
    private String nom, role;
    private double taille;

    public Ewok(String nom, double taille, String role) {
        this.nom = nom;
        this.role = role;
        this.taille = taille;
    }

    @Override
    public String toString() {
        return "Ewok{" +
                "nom='" + nom + '\'' +
                ", role='" + role + '\'' +
                ", taille=" + taille +
                '}';
    }

    @Override
    public String getRace() {
        return "Ewok";
    }

    @Override
    public double getTaille() {
        return taille;
    }

    @Override
    public String getCaracteristique() {
        return role;
    }

    @Override
    public String getNom() {
        return nom;
    }
}
