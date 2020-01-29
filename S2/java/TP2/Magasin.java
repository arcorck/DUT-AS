public class Magasin { 
    private String nom;
    private boolean ouvertLundi, ouvertDimanche ;

    public Magasin(String nom, boolean lundi, boolean dimanche) {
        this.nom = nom;
        this.ouvertLundi = lundi;
        this.ouvertDimanche = dimanche;
    }

    public String getnom(){
        return this.nom;
    }

    public boolean ouvertlundi ( ){
        return this.ouvertLundi;
    }

    public boolean ouvertdimanche ( ){
        return this.ouvertDimanche;
    }

    public String toString() {
        String res = "Le magasin ";
        res += this.getnom();
        if (this.ouvertlundi()){
            res += " est ouvert le lundi";
        }else{
            res += " n'est pas ouvert le lundi";
        }
        if (this.ouvertdimanche()){
            res += " et est ouvert le dimanche";
        }else{
            res += " et n'est pas ouvert le dimanche";
        }
        return res;
    }
}