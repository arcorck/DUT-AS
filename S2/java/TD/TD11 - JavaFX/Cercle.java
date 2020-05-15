package sample;

import javafx.scene.paint.Color;
import javafx.scene.shape.Circle;
import java.util.List;

public class Cercle extends Circle {

    private static double RAYON_MINI = 0.1;

    public Cercle(double largeur, double hauteur){
        super(largeur, hauteur, RAYON_MINI);
        this.setFill(new Color(Math.random(), Math.random(), Math.random(), 1.0));
    }

    public Cercle (double largeur, double hauteur, List<Cercle> lescercles){
        super(largeur, hauteur, RAYON_MINI);
        this.setFill(new Color(Math.random(), Math.random(), Math.random(), 1.0));
        placerAuHasard(lescercles, largeur, hauteur);
        this.grossirrayonDicho(lescercles, largeur, hauteur);
    }

    public void grossir(List<Cercle> liste, double largeur, double hauteur){
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

    private boolean intersecte(Cercle c){
        double distance = Math.sqrt( (this.getCenterX()-c.getCenterX())*(this.getCenterX()-c.getCenterX()) +(this.getCenterY()-c.getCenterY())*(this.getCenterY()-c.getCenterY()));
        double sommeRayon = this.getRadius()+c.getRadius();
        return (Math.abs(distance) < sommeRayon);
    }

    private boolean estDansLeCadre(double largeur, double hauteur){
        double centreX = this.centerXProperty().getValue().intValue();
        double centreY = this.centerYProperty().getValue().intValue();
        return (centreX - this.getRadius() > 0 && centreX + this.getRadius() < largeur && centreY - this.getRadius() > 0 && centreY + this.getRadius() < hauteur);
    }

    private boolean estValide(List<Cercle> liste, double largeur, double hauteur){
        if (!this.estDansLeCadre(largeur, hauteur)){
            return false;
        }
        if (!liste.isEmpty()) {
            for (Cercle c : liste) {
                if (this.intersecte(c)) {
                    return false;
                }
            }
        }
        return true;
    }

    private void placerAuHasard(List<Cercle> liste, double l, double h){
        if(!liste.isEmpty()) {
            boolean ok = true;
            do {
                ok = true;

                System.out.println("placeAuHasard");
                double x = Math.random() * l;
                double y = Math.random() * h;
                this.setCenterX(x);
                this.setCenterY(y);
                for (Cercle c : liste) {
                    if (!estValide(liste, l, h)) {
                        ok = false;
                    }
                }
            } while (!ok);
            this.setFill(new Color(Math.random(), Math.random(), Math.random(), 1.0));
        }
    }
}
