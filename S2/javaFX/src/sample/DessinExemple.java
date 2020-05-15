package sample;

import javafx.application.Application;
import javafx.scene.Group; 
import javafx.scene.layout.BorderPane;
import javafx.scene.Scene; 
import javafx.stage.Stage; 
import javafx.scene.paint.Color;
import java.awt.*;
import java.util.List;
import java.util.ArrayList;
import javafx.scene.control.Label;
import javafx.scene.layout.VBox;
import javafx.geometry.Pos;


public class DessinExemple extends Application {
    
    private int largeur = 1000;
    private int hauteur = 500;
    private List<Rect> liste;
    
    // === Début du code à compléter / modifier ===========

    @Override
    public void init(){
        this.liste = new ArrayList<>();
        Rect c;
        for(int i = 0; i < 2; ++i) {
            c = new Rect(largeur, hauteur, liste);
            this.liste.add(c);
        }
    }

    // === Fin du code à compléter / modifier ===========
     
    @Override 
    public void start(Stage stage) { 
       Group dessinCercles = new Group();
       dessinCercles.getChildren().addAll(this.liste);
       BorderPane root = new BorderPane();
       root.setCenter(dessinCercles);
       VBox infos =this.informations();
       root.setBottom(infos);
       root.setAlignment(infos, Pos.TOP_LEFT);
       Scene scene = new Scene(root, this.largeur, this.hauteur+infos.getHeight()+40);  
       stage.setTitle("Formes");
       stage.setScene(scene);
       stage.show();         
    }   
      
    private VBox informations(){
        VBox vbox = new VBox();
        String cssLayout = "-fx-border-color: black;\n" + "-fx-border-width: 2;\n";
        vbox.setStyle(cssLayout);
        /*vbox.getChildren().add(new Label("Le Cercle le plus petit est : " + BibCercles.getMin(liste)));
        vbox.getChildren().add(new Label("La surface du plus petit cercle est : " + Math.round(BibCercles.getsurfaceMin(liste)*100.0)/100.0));
        vbox.getChildren().add(new Label("La surface du plus grand cercle est : " + Math.round(BibCercles.getsurfaceMax(liste)*100.0)/100.0));
        vbox.getChildren().add(new Label("La surface totale de tout les cercles est : " + Math.round(BibCercles.surfaceTotale(liste)*100.0)/100.0));
        vbox.getChildren().add(new Label("Le rayon moyen est : " + BibCercles.RayonMoyen(liste)));*/
        return vbox;      
    }
    
    public static void main(String args[]){ 
       launch(args); 
   } 
}       
