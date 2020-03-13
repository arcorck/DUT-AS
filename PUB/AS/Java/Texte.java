import java.util.ArrayList;

class Texte{

  private ArrayList<Lettre> texte;
  
  public Texte(String s){
      this.texte = new ArrayList<Lettre>();
      char c;
      for(int i=0; i<s.length(); ++i){
          c = s.charAt(i);
          texte.add(new Lettre(c));
      }
  }
  
  public String toString(){
      String res="";
      for(Lettre l : texte){
          res += l.getLettre();
      }
      return res;
  }

  public String toMorse(){
      String code="";
      for(Lettre l : texte){
          if(!code.equals("")){
              code+="___";
          }
          code += l.toMorse();
      }
      return code;
  }
  
  public boolean contient(Lettre l){
      return this.texte.contains(l);
  }
  
  public static String decode(String code){
      
      String[] lesMots = code.split("_______");
      String res = "";
      for(String m : lesMots){
          System.out.println(m);          
          String [] lesLettres = m.split("___");
          for(String s : lesLettres){
              System.out.println(s);          
              res += Lettre.toChar(s);
          }
          res +=" ";
      }
      return res;
  } 
  
  public void toSon(){
      Son leSon = new Son();
      String code = this.toMorse();
      for(int i=0; i<code.length(); ++i){
          char c = code.charAt(i);
          if(c=='_'){
              leSon.pause();
          }
          else{
              leSon.tone(100);
          }
      }
  } 
  
  static public void main(String [] args){
      Lettre l = new Lettre('a');
      Texte m = new Texte("il fait beau");
      String codage = m.toMorse();
      System.out.println(codage);
      System.out.println(Texte.decode(codage));
      Lettre z = new Lettre('z');
      Lettre a = new Lettre('a');

      System.out.println(m.contient(a));
      System.out.println(m.contient(z));
      
      //m.toSon();
      
      m = new Texte("sos sos sos sos");
      System.out.println(m.toMorse());
      
      m.toSon();
      
  }
  
}
