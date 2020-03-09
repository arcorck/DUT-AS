public class CoupleEntiers {
    private int premier, second;

    public CoupleEntiers() {
        this.premier = 0;
        this.second = 1;
    }

    public CoupleEntiers(int a, int b) {
        this.premier = a;
        this.second = b;
    }

    public void setPrem(int premier) {
        this.premier = premier;
    }

    public void setSec(int sec){
        this.second = sec;
    }

    public void permute() {
        int aux;
        aux = this.premier;
        this.premier = this.second;
        this.second = aux;
    }

    public int getPrem(){
        return this.premier;
    }

    public int getSec() {
        return this.second;
    }

    public int fraction() {
        return this.premier / this.second;
    }

    public String toString() {
        return "Couple : (" + this.premier + "," + this.second + ")";
    }

    public int somme (){
        return this.getPrem() + this.getSec();
    }

    public CoupleEntiers plus (CoupleEntiers b){
        return new CoupleEntiers(this.getPrem() + b.getPrem(), this.getSec() + b.getSec());
    }
}