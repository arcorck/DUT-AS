import java.util.ArrayList;

class Lettre{
    private char laLettre;
    private static ArrayList<String> codeMorse = new ArrayList<String>() ;
    static{
        codeMorse.add("=_===");
        codeMorse.add("===_=_=_="); 
        codeMorse.add("===_=_===_="); 
        codeMorse.add("===_=_="); 
        codeMorse.add("="); 
        codeMorse.add("=_=_===_="); 
        codeMorse.add("===_===_="); 
        codeMorse.add("=_=_=_="); 
        codeMorse.add("=_="); 
        codeMorse.add("=_===_===_===");
        codeMorse.add("===_=_==="); 
        codeMorse.add("=_===_=_="); 
        codeMorse.add("===_==="); 
        codeMorse.add("===_="); 
        codeMorse.add("===_===_==="); 
        codeMorse.add("=_===_===_=");
        codeMorse.add("===_===_=_==="); 
        codeMorse.add("=_===_="); 
        codeMorse.add("=_=_="); 
        codeMorse.add("==="); 
        codeMorse.add("=_=_==="); 
        codeMorse.add("=_=_=_==="); 
        codeMorse.add("=_===_==="); 
        codeMorse.add("===_=_=_==="); 
        codeMorse.add("===_=_===_==="); 
        codeMorse.add("===_===_=_="); 
    } 
    
    public Lettre(char a){
        this.laLettre = a;
    }
    
    public Lettre(String code){
        this.laLettre = Lettre.toChar(code);
    }
    
    public char getLettre(){
        return this.laLettre;
    }

    public int toAscii(){
        return (int)this.laLettre - (int)('a');
    }
    
    public String toMorse(){
        String res;
        if(this.laLettre == ' '){
            res = "_";
        }
        else{
            res = this.codeMorse.get(this.toAscii());
        }
        return res;
    }
   
    public String toMorsebis(){
        String res="_";
        // un espace en standard
        switch (laLettre) {
            case 'a' : res = "=_==="; 
                       break;
            case 'b' : res = "===_=_=_="; 
                       break;
            case 'c' : res = "===_=_===_="; 
                       break;
            case 'd' : res = "===_=_="; 
                       break;
            case 'e' : res = "="; 
                       break;
            case 'f' : res = "=_=_===_="; 
                       break;
            case 'g' : res = "===_===_="; 
                       break;
            case 'h' : res = "=_=_=_="; 
                       break;
            case 'i' : res = "=_="; 
                       break;
            case 'j' : res = "=_===_===_==="; 
                       break;            
            case 'k' : res = "===_=_==="; 
                       break;
            case 'l' : res = "=_===_=_="; 
                       break;
            case 'm' : res = "===_==="; 
                       break;
            case 'n' : res = "===_="; 
                       break;
            case 'o' : res = "===_===_==="; 
                       break;
            case 'p' : res = "=_===_===_="; 
                       break;
            case 'q' : res = "===_===_=_==="; 
                       break;
            case 'r' : res = "=_===_="; 
                       break;
            case 's' : res = "=_=_="; 
                       break;
            case 't' : res = "==="; 
                       break;              
            case 'u' : res = "=_=_==="; 
                       break;
            case 'v' : res = "=_=_=_==="; 
                       break;
            case 'w' : res = "=_===_==="; 
                       break;
            case 'x' : res = "===_=_=_==="; 
                       break;
            case 'y' : res = "===_=_===_==="; 
                       break;
            case 'z' : res = "===_===_=_="; 
                       break;                  
        }
        return res;
    }
    public static char toChar(String code){
        char res=' ';
        int pos = Lettre.codeMorse.indexOf(code);
        if(pos != -1){
            pos = pos +(int)('a');
            res = (char)(pos);
        }
        return res;
    }
    
    public static char toCharBis(String code){
        char res=' ';
        // un espace en standard
        switch (code) {
            case "=_===" : res = 'a'; 
                       break;
            case "===_=_=_=" : res = 'b'; 
                       break;
            case "===_=_===_=" : res = 'c'; 
                       break;
            case "===_=_=" : res = 'd'; 
                       break;
            case "=" : res = 'e'; 
                       break;
            case "=_=_===_=" : res = 'f'; 
                       break;
            case "===_===_=" : res = 'g'; 
                       break;
            case "=_=_=_=" : res = 'h'; 
                       break;
            case "=_=" : res = 'i'; 
                       break;
            case "=_===_===_===" : res = 'j'; 
                       break;            
            case "===_=_===" : res = 'k'; 
                       break;
            case "=_===_=_=" : res = 'l'; 
                       break;
            case "===_===" : res = 'm'; 
                       break;
            case "===_=" : res = 'n'; 
                       break;
            case "===_===_===" : res = 'o'; 
                       break;
            case "=_===_===_=" : res = 'p'; 
                       break;
            case "===_===_=_===" : res = 'q'; 
                       break;
            case "=_===_=" : res = 'r'; 
                       break;
            case "=_=_=" : res = 's'; 
                       break;
            case "===" : res = 't'; 
                       break;              
            case "=_=_===" : res = 'u'; 
                       break;
            case "=_=_=_===" : res = 'v'; 
                       break;
            case "=_===_===" : res = 'w'; 
                       break;
            case "===_=_=_===" : res = 'x'; 
                       break;
            case "===_=_===_===" : res = 'y'; 
                       break;
            case "===_===_=_=" : res = 'z'; 
                       break;                  
        }
        return res;
    }
    
    public boolean equals(Object obj){
        if(obj == null){
            return false;
        }
        if (!(obj instanceof Lettre)){
            return false;
        }
        Lettre l = (Lettre)obj;
        return this.laLettre==l.laLettre;
    }
       
    public static void main(String [] args){
        Lettre a = new Lettre('a');
        Lettre z = new Lettre('z');
        System.out.println("a est " + a.toAscii() + a.toMorse());
        System.out.println("z est " + z.toAscii() + z.toMorse());
        
        System.out.println("lettre : ===_===_=== est "+ Lettre.toChar("===_===_==="));
        
        Lettre g = new Lettre("===_===_=");
        System.out.println("g est " + g.toAscii() + g.toMorse());

    }
}


        
