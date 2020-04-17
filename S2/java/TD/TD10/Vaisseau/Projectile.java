public class Projectile {
    private String nom;
    private int position;

    public Projectile(String nom, int position) {
        this.nom = nom;
        this.position = position;
    }

    public Projectile() {
        this.nom = "name";
        this.position = 0;
    }

    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public int getPosition() {
        return position;
    }

    public void setPosition(int position) {
        this.position = position;
    }
}
