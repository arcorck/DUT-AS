package sample;

import javafx.scene.paint.Color;
import javafx.scene.shape.Rectangle;
import java.util.List;

public class Rect extends Rectangle {

    //private static double RAYON_MINI = 0.1;

    /*public Rect(int largeur, int hauteur){
        super(Math.random() * largeur, Math.random() * hauteur);
        this.setFill(new Color(Math.random(), Math.random(), Math.random(), 1.0));
    }*/

    public Rect(int largeur, int hauteur){
        super(Math.random() * largeur, Math.random() * hauteur,100, 50);
        this.setFill(new Color(Math.random(), Math.random(), Math.random(), 1.0));
    }

    public Rect (double largeur, double hauteur, List<Rect> lesrects){
        super(largeur * Math.random(), hauteur * Math.random());
        this.setFill(new Color(Math.random(), Math.random(), Math.random(), 1.0));
        System.out.println(estValide(lesrects, largeur, hauteur));
        //placerAuHasard(lesrects, largeur, hauteur);
        //this.grossirrayonDicho(lescercles, largeur, hauteur);
    }

    /*public void grossir(List<Cercle> liste, double largeur, double hauteur){
        while (this.estValide(liste, largeur, hauteur)){
            this.setRadius(this.getRadius()+RAYON_MINI);
        }
        if (!this.estValide(liste, largeur, hauteur)){
            this.setRadius(this.getRadius()-RAYON_MINI);
        }
    }

    public void grossirrayonDicho (List<Cercle> liste ,double l, double h){
        double rayonmax = Math.min(l,h);
        boolean possible = true;
        while (possible && rayonmax > RAYON_MINI){
            this.setRadius(rayonmax);
            if (this.estValide(liste, l, h)){
                possible = false;
            }else{
                rayonmax = rayonmax/2;
            }
        }
    }

    */private boolean intersecte(Rect r){
        return !(this.intersects(r.getX(), r.getY(), r.getWidth(), r.getHeight()));
    }

    private boolean estDansLeCadre(double largeur, double hauteur){
        double X = this.getX();
        double Y = this.getY();
        return !(X > 0 && X + this.getWidth() < largeur && Y> 0 && Y + this.getHeight() < hauteur);
    }

    private boolean estValide(List<Rect> liste, double largeur, double hauteur){
        if (!this.estDansLeCadre(largeur, hauteur)){
            return false;
        }
        if (!liste.isEmpty()) {
            for (Rect r : liste) {
                if (this.intersecte(r)) {
                    return false;
                }
            }
        }
        return true;
    }

    private void placerAuHasard(List<Rect> liste, double l, double h){
        if(!liste.isEmpty()) {
            boolean ok = true;
            do {
                ok = true;
                double x = Math.random() * l;
                double y = Math.random() * h;
                this.setX(l);
                this.setY(h);
                for (Rect r : liste) {
                    if (!estValide(liste, l, h)) {
                        ok = false;
                    }
                }
            } while (!ok);
            this.setFill(new Color(Math.random(), Math.random(), Math.random(), 1.0));
        }
    }
}
