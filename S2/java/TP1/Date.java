public class Date {
   private int jour, mois, annee;

   public Date(int j, int m, int a) {
       this.jour = j;
       this.mois = m;
       this.annee = a;
   }

   public int getJour() {
       return this.jour;
   }

   public int getMois() {
       return this.mois;
   }

   public int getAnnee() {
       return this.annee;
   }

   public boolean bissextile() {
       if (this.getAnnee() % 4 == 0) {
           if (this.getAnnee() % 400 != 0){
               return true;
           }
           else{
               return false;
           }
       }else{
           return false;
       }
   }

   public int nbJourMois() {
       if (this.getMois() < 1 || this.getMois() > 12 || this.getJour() < 1 || this.getJour() > 31){
           return -1;
       }else{
           if (this.getMois() == 1 || this.getMois() == 3 || this.getMois() == 5 || this.getMois() == 7 || this.getMois() == 8 || this.getMois() == 10 || this.getMois() == 12){
                return 31;
            }else{
                if (this.getMois() == 4 || this.getMois() == 6 || this.getMois() == 9 || this.getMois() == 11 ){
                    return 30;
                }else{
                    if (this.bissextile()){
                        return 29;
                    }else{
                        return 28;
                    }
                }
            }  
       }
   }

   public boolean valide() {
       if (this.mois > 12 || this.mois < 1 || this.nbJourMois() == -1){
           return false;
       }
       if (this.getMois() == 1 || this.getMois() == 3 || this.getMois() == 5 || this.getMois() == 7 || this.getMois() == 8 || this.getMois() == 10 || this.getMois() == 12){
           return this.nbJourMois() == 31;
       }else{
           if (this.getMois() == 4 || this.getMois() == 6 || this.getMois() == 9 || this.getMois() == 11 ){
               return this.nbJourMois() == 30;
           }else{
               if (this.bissextile()){
                   return this.nbJourMois() == 29;
               }else{
                   return this.nbJourMois() == 28;
               }
           }
        }  
    }


    public Date lendemain (){
        Date lendemain = new Date (this.getJour()+1, this.getMois(), this.getAnnee());
        if (lendemain.valide()){
            return lendemain;
        }else{
            return null;
        }
    }
   public String toString() {
       return this.getJour() + "/" + this.getMois() + "/" + this.getAnnee();
   }

}