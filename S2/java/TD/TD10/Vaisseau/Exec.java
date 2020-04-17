public class Exec {

    public static void main(String[] args) {
        Vaisseau v = new Vaisseau(2, 4, 9);
        Vaisseau v2 = new Vaisseau(12, 14, 19);
        try{
            v.deplacer(-1);
            v.deplacer(-1);
            v.deplacer(-1);
            System.out.println("3 déplacemnts ok");
        }catch(DeplacementImpossible e) {
            System.out.println("Le deplacement est impossible");
        }
        try{
            for (int i = 0; i < 5; i++){
                v.tirer();
            }
            System.out.println("5 tirs ok");
        }catch(PlusdeProjectileException e){
            System.out.println("Le vaisseau n'a plus de projectiles");
        }
        try{
            for (int i = 0; i < 10; i++){
                v.retirerPointDeVie();
            }
            System.out.println("10 retraits de point de vie ok");
        }catch(PlusdePointsdeVieException e) {
            System.out.println("Le vaisseau n'a plus de points de vie");
        }

        try{
            v2.deplacer(-1);
            v2.deplacer(-1);
            v2.deplacer(-1);
            System.out.println("3 déplacemnts ok");
        }catch(DeplacementImpossible e) {
            System.out.println("Le deplacement est impossible");
        }
        try{
            for (int i = 0; i < 5; i++){
                v2.tirer();
            }
            System.out.println("5 tirs ok");
        }catch(PlusdeProjectileException e){
            System.out.println("Le vaisseau n'a plus de projectiles");
        }
        try{
            for (int i = 0; i < 10; i++){
                v2.retirerPointDeVie();
            }
            System.out.println("10 retraits de point de vie ok");
        }catch(PlusdePointsdeVieException e) {
            System.out.println("Le vaisseau n'a plus de points de vie");
        }
    }
}
