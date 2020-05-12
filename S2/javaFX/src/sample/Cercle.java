package sample;

import javafx.scene.shape.Circle;

import java.util.List;

public class Cercle extends Circle {

    private static double RAYON_MINI = 30.0;

    public Cercle(double largeur, double hauteur){
        super(largeur, hauteur, RAYON_MINI);
    }

    private boolean intersecte(Cercle c){
        double distanceX = this.centerXProperty().getValue().intValue() - c.centerXProperty().getValue().intValue();
        double distanceY = this.centerYProperty().getValue().intValue() - c.centerYProperty().getValue().intValue();
        double sommeRayon = this.getRadius()+c.getRadius();
        return (Math.abs(distanceX) < sommeRayon || Math.abs(distanceY) < sommeRayon);
    }

    private boolean estDansLeCadre(double largeur, double hauteur){
        double centreX = this.centerXProperty().getValue().intValue();
        double centreY = this.centerYProperty().getValue().intValue();
        return (centreX - RAYON_MINI > 0 && centreX + RAYON_MINI < largeur && centreY - RAYON_MINI > 0 && centreY + RAYON_MINI < hauteur);
    }

    private boolean estValide(List<Cercle> liste, double largeur, double hauteur){
        for (Cercle c : liste){
            if (this.intersecte(c)){
                return false;
            }
        }
        if (!this.estDansLeCadre(largeur, hauteur)){
            return false;
        }
        return true;
    }

    private void placerAuHasard(List<Cercle> liste, double largeur, double hauteur){

    }
}
