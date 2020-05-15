package sample;

import java.util.List;

public class BibCercles {

    public static Cercle getMin(List<Cercle> liste){
        if (!liste.isEmpty()){
            double rayonmin = liste.get(0).getRadius();
            Cercle res = new Cercle(0, 0);
            for (Cercle c : liste){
                if (c.getRadius() < rayonmin){
                    rayonmin = c.getRadius();
                    res = c;
                }
            }
            return res;
        }else{
            return null;
        }
    }

    public static double getsurfaceMax(List<Cercle> liste){
        if (!liste.isEmpty()){
            double rayonmax = liste.get(0).getRadius();
            for (Cercle c : liste){
                if (c.getRadius() > rayonmax){
                    rayonmax = c.getRadius();
                }
            }
            return Math.pow(rayonmax, 2) * Math.PI;
        }else{
            return -1;
        }
    }

    public static double getsurfaceMin(List<Cercle> liste){
        if (!liste.isEmpty()){
            double rayonmin = liste.get(0).getRadius();
            for (Cercle c : liste){
                if (c.getRadius() < rayonmin){
                    rayonmin = c.getRadius();
                }
            }
            return Math.pow(rayonmin, 2) * Math.PI;
        }else{
            return -1;
        }
    }

    public static double surfaceTotale(List<Cercle> liste){
        if (liste.isEmpty()){
            return 0.0;
        }else {
            double surface = 0.0;
            for (Cercle c : liste){
                surface += Math.pow(c.getRadius(), 2) * Math.PI;
            }
            return surface;
        }
    }

    public static double RayonMoyen (List<Cercle> liste){
        if (!liste.isEmpty()){
            double rayonmoyen = liste.get(0).getRadius();
            for (Cercle c : liste){
                rayonmoyen += c.getRadius();
            }
            return rayonmoyen/liste.size();
        }else{
            return -1;
        }
    }
}
