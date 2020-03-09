class Projectile{
    int posx, posy;

    Projectile (int x, int y){
        this.posx = x;
        this.posy = y;
    }

    public String toString(){
        return "Projectile à la proposition : (" + this.posx + "," + this.posy + ")";    
    }
}