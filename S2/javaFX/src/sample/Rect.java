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
        super(Math.random() * largeur, Math.random() * hauteur, Math.random() * largeur, Math.random() * hauteur);
        this.setFill(new Color(Math.random(), Math.random(), Math.random(), 1.0));
        placerAuHasard(lesrects, largeur, hauteur);
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
        double distanceL = Math.abs(this.getX() - r.getX());
        double distanceH = Math.abs(this.getY() - r.getY());
        boolean largeurok = distanceL > r.getWidth()/2 + this.getWidth()/2;
        boolean hauteureurok = distanceH > r.getHeight()/2 + this.getHeight()/2;
        return largeurok && hauteureurok;
    }

    private boolean estDansLeCadre(double largeur, double hauteur){
        double centreX = this.getX();
        double centreY = this.getY();
        return (centreX - this.getWidth()/2 > 0 && centreX + this.getWidth()/2 < largeur && centreY - this.getHeight()/2 > 0 && centreY + this.getHeight()/2 < hauteur);
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
