public class Vecteur3F{
    double x, y, z;

    public Vecteur3F (double a, double b, double c){
        this.x = a;
        this.y = b;
        this.z = c;
    }

    public double getx(){
        return this.x;
    }

    public double gety(){
        return this.y;
    }

    public double getz(){
        return this.z;
    }

    public void setx(double a){
        this.x = a;
    }

    public void sety(double a){
        this.y = a;
    }

    public void setz(double a){
        this.z = a;
    }

    public String toString(){
        double produit = Math.pow(this.getx(),2) + Math.pow(this.gety(), 2) + Math.pow(this.getz(), 2);
        double norme = Math.sqrt(produit);
        return "Vecteur3f : <" + this.getx() + " " + this.gety() + " " + this.getz() + "> De norme : " + norme;
    }

    public void modif(double val, int comp){
        if (comp == 1){
            this.setx(val);
        }
        if (comp == 2){
            this.sety(val);
        }
        if (comp == 3){
            this.setz(val);
        }
    }
}
