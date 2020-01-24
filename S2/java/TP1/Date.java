public class Date {
   private int jour, mois, annee;

   public Date(int j, int m, int a) {//TODO}

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
       return this.getAnnee() % 4 == 0 and this.getAnnee() % 400 != 0;
   }

   public int nbJourMois() {
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

   public boolean valide() {
       
   }

   public String toString() {
       return this.getJour() + "/" + this.getMois() + "/" + this.getAnnee();
   }

}