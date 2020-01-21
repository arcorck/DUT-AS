public class CompteBancaire{
    private String proprietaire;
	private int solde;
	private String type;
	
	public CompteBancaire (String nom){
		this.proprietaire = nom;
		this.solde = 0;
		this.type ="";
	}
	
	public CompteBancaire (String nom, int solde){
		this.proprietaire = nom;
		this.solde = solde;
		this.type="";
	}
	
	public CompteBancaire (String nom, int solde, String type){
		this.proprietaire = nom;
		this.solde = solde;
		this.type=type;
	}
	
	public int getSolde(){
		return this.solde;
	}
	
	public void deposer (int somme){
		this.solde+=somme;
	}
	
	public void retirer (int somme){
		this.solde-=somme;
	}
	
	public String toString (){
		return ("Il reste " + this.getSolde() + " euros à " + this.proprietaire);
	}
}
