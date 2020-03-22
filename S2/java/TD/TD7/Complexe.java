public class Complexe{
    private double re;
    private double im;

    public Complexe(double re, double im) {
        this.re=re;
        this.im=im; 
    }

    public double getReel(){
        return this.re;
    }

    public double getImag(){
        return this.im;
    }

    public String toString(){
        String res = "";
        if (this.re != 0){
            res += Double.toString(this.re);
        }
        if (this.im > 0){
            res += " + " + Double.toString(this.im) + "i";
        }else{
            if (this.im < 0){
                res += " - " + Double.toString(-1 * this.im) + "i";
            }
        }
        res += "\n";
        return res;
    }
    
}