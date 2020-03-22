public class Chien{
    private String nom, couleur;
    private int longueur;

    public Chien (String n, int l, String c){
        this.nom =n;
        this.couleur = c;
        this.longueur = l;
    }

    public String getNom(){
        return this.nom;
    }

    public String getCouleur(){
        return this.couleur;
    }

    public int getLongueur(){
        return this.longueur;
    }

    @Override
    public boolean equals(Object ch2){
        if(ch2 instanceof Chien){
            return this.nom.equals(((Chien)ch2).nom);
        }
        else{
            return false;
        }
    }

    @Override
    public int hashCode(){
        return this.nom.hashCode()+this.couleur.hashCode()+this.longueur;
    }

    public String toString(){
        return this.nom + " est de couleur " + this.couleur + " et à des poils de " + this.longueur + " cm\n";
    }

    public static void main(String[] arg){
        Chien medor = new Chien("Médor", 15, "brune");
        System.out.println(medor);
    }
}