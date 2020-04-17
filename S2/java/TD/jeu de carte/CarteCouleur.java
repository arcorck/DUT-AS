public class CarteCouleur implements Carte{
    private String couleur;
    private int valeur;

    public CarteCouleur (String c, int v){
        this.couleur = c;
        this.valeur = v;
    }

    public String getValeur(){
        switch (this.valeur) {
            case 1:
                return("As");
            case 2:
                return("Deux");
            case 3:
                return("Trois");
            case 4:
                return("Quatre");
            case 5:
                return("Cinq");
            case 6:
                return("Six");
            case 7:
                return("Sept");
            case 8:
                return("Huit");
            case 9:
                return("Neuf");
            case 10:
                return("Dix");
            case 11:
                return("Valet");
            case 12:
                return("Dame");
            case 13:
                return("Roi");
            default:
                return "erreur";
        }
    }

    @Override
    public String getType() {
        return "Carte Couleur";
    }

    public int getValeurInt(){
        return this.valeur;
    }

    public String toString(){
        return this.getValeur() + " de " + this.couleur;
    }
}
