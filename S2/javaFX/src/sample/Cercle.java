package sample;

import javafx.scene.paint.Color;
import javafx.scene.shape.Circle;

import java.util.ArrayList;
import java.util.List;

public class Cercle extends Circle {

    private static double RAYON_MINI = 30.0;

    public Cercle(double largeur, double hauteur){
        super(largeur, hauteur, RAYON_MINI);
        this.setFill(new Color(Math.random(), Math.random(), Math.random(), 1.0));
    }

    public Cercle (double largeur, double hauteur, List<Cercle> lescercles){
        super(largeur, hauteur, RAYON_MINI);
        this.setFill(new Color(Math.random(), Math.random(), Math.random(), 1.0));
        placerAuHasard(lescercles, largeur, hauteur);
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
        for (Cercle c : liste){
            if (this.intersecte(c)){
                return false;
            }
        }
        return true;
    }

    private void placerAuHasard(List<Cercle> liste, double largeur, double hauteur){
        double l = Math.random() * largeur;
        double h = Math.random() * hauteur;
        while (!estValide(liste, l, h)){
            l = Math.random() * largeur;
            h = Math.random() * hauteur;
        }
        liste.add(new Cercle(l, h));
    }
}
