public class ExecutableComplexe {
  public static void main(String [] args) {
       Complexe complexe1 = new Complexe(5, -6);
       Complexe complexe2 = new Complexe(2, -4);
       Complexe complexe3 = new Complexe(4/2, -4);
       System.out.println(complexe1.getReel()+ " "+ complexe2.getImag());
       complexe1.afficheCartesien();
       // affiche (5, -6)
       complexe2.afficheComplexe();
       // affiche 2 +i -4
       complexe1.somme(complexe2).afficheComplexe();
       System.out.println(complexe2.egal(complexe3));       
       System.out.println(complexe2 == complexe3); //false car on compare les adresses mémoire 
  }
}