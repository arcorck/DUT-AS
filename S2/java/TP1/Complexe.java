public class Complexe{
    int reel, imaginaire;

    public Complexe (int re, int im){
        this.reel = re;
        this.imaginaire = im;
    }

    public int getReel (){
        return this.reel;
    }

     public int getImag (){
        return this.imaginaire;
    }

    public void afficheCartesien(){
        System.out.println("(" + this.getReel() + "," + this.getImag() + ")");
    }

    public void afficheComplexe(){
        System.out.println(this.getReel() + " + i " + this.getImag());
    }

    public Complexe somme (Complexe a){
        return new Complexe(this.getReel() + a.getReel(), this.getImag() + a.getImag());
    }

    public boolean egal (Complexe a){
        return this.getReel() == a.getReel() && this.getImag() == a.getImag();
    }
}