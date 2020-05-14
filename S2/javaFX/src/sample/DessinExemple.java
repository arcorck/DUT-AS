package sample;

import javafx.application.Application;
import javafx.scene.Group; 
import javafx.scene.layout.BorderPane;
import javafx.scene.Scene; 
import javafx.stage.Stage; 
import javafx.scene.paint.Color;
import java.util.List;
import java.util.ArrayList;
import javafx.scene.shape.Circle;
import javafx.scene.control.Label;
import javafx.scene.layout.VBox;
import javafx.geometry.Pos;


public class DessinExemple extends Application {
    
    private int largeur = 600;
    private int hauteur = 300;
    private List<Cercle> liste;
    
    // === Début du code à compléter / modifier ===========

    @Override
    public void init(){
        this.liste = new ArrayList<>();
        Cercle c;
        for(int i = 0; i < 10; ++i) {
            c = new Cercle(largeur, hauteur, liste);
            //this.liste.add(c);
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
        // Code à compléter à patir de la Q17
        vbox.getChildren().add(new Label("Le Cercle le plus petit est : " ));
        vbox.getChildren().add(new Label("La surface totale est : ")); 
        return vbox;      
    }
    
    public static void main(String args[]){ 
       launch(args); 
   } 
}       
