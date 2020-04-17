public class Vaisseau {

    private int position, nb_projectiles, nb_points_de_vie;

    public Vaisseau(int position, int nb_projectiles, int nb_points_de_vie) {
        this.position = position;
        this.nb_projectiles = nb_projectiles;
        this.nb_points_de_vie = nb_points_de_vie;
    }

    public void deplacer (int deplacement) throws DeplacementImpossible{
        if (this.position + deplacement < 0){
            throw new DeplacementImpossible();
        }
        else{
            position = position + deplacement;
        }
    }

    public void deplacer20foisagauche (){
        try{
            for (int i = 0; i < 20; i++){
                deplacer(-1);
            }
        }catch (DeplacementImpossible e){
            System.out.println("Le vaisseau est deja tout à gauche");
        }
    }

    public Projectile tirer () throws PlusdeProjectileException{
        if (nb_projectiles == 0){
            throw new PlusdeProjectileException();
        }else{
            this.nb_projectiles--;
            return new Projectile("projectile", this.position);
        }
    }

    public void retirerPointDeVie () throws PlusdePointsdeVieException{
        if (this.nb_points_de_vie == 0){
            throw new PlusdePointsdeVieException();
        }else{
            this.nb_points_de_vie--;
        }
    }
}
