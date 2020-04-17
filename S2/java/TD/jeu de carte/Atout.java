public class Atout implements Carte{
    private int valeur;

    public Atout (int v){
        this.valeur = v;
    }

    @Override
    public String getType() {
        return "Atout";
    }

    @Override
    public int getValeurInt() {
        return this.valeur;
    }

    public String getValeur() {
        switch (this.valeur) {
            case 1:
                return("Petit");
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
                return("Onze");
            case 12:
                return("Douze");
            case 13:
                return("Treize");
            case 14:
                return("Quatorze");
            case 15:
                return("Quinze");
            case 16:
                return("Seize");
            case 17:
                return("Dix-Sept");
            case 18:
                return("Dix-Huit");
            case 19:
                return("Dix-Neuf");
            case 20:
                return("Vingt");
            case 21:
                return("Vingt-Et-Un");
            case 22:
                return("Excuse");
            default:
                return "erreur";
        }
    }

    public void setValeur(int valeur) {
        this.valeur = valeur;
    }

    @Override
    public String toString() {
        return "Atout{" +
                "valeur=" + valeur +
                '}';
    }
}
