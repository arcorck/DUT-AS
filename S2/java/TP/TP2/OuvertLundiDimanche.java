public class OuvertLundiDimanche {
    private boolean lundi, dimanche;

    public OuvertLundiDimanche (boolean lundi, boolean dimanche) {
        this.lundi = lundi;
        this.dimanche = dimanche;
    }

    public boolean getLundi(){
        return this.lundi;
    }

    public boolean getDimanche(){
        return this.dimanche;
    }

    public String toString() {
        String res = "";
        if (this.lundi){
            res += " est ouvert le lundi";
        }else{
            res += " n'est pas ouvert le lundi";
        }
        if (this.dimanche){
            res += " et est ouvert le dimanche";
        }else{
            res += " et n'est pas ouvert le dimanche";
        }
        return res;
    }
}
