public class Carte{
    private int valeur;
    private String couleur;

    public Carte (int valeur, String couleur){
        this.valeur = valeur;
        this.couleur = couleur;
    }

    public String getCouleur(){
        return this.couleur;
    }

    public String getValeur(){
        return Integer.toString(this.valeur);
    }

    public int getValeurInt(){
        return this.valeur;
    }
}