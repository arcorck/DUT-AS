public class ExecZoo {
    public static void main(String[] args) throws NestpasBlesseException {
        Animal loup = new Animal("loup", false);
        Animal panda = new Animal("panda", true);
        Animal gorille = new Animal("gorille", false);
        Animal toucan = new Animal("toucan", true);
        Animal rat = new Animal("rat", true);
        Zoo zoo = new Zoo("Beauval");
        zoo.acceuillir(loup);
        zoo.acceuillir(panda);
        zoo.acceuillir(gorille);
        zoo.acceuillir(toucan);
        System.out.println(zoo);
        try{
            zoo.soigner(rat);
            System.out.println("le rat a bien été soigné");
        }catch(NestpasdansleZooException e){
            System.out.println("Le rat n'est pas dans le zoo");
        }catch(NestpasBlesseException e){
            System.out.println("Le rat n'est pas bléssé");
        }
        try{
            zoo.soigner(loup);
            System.out.println("le loup a bien été soigné");
        }catch(NestpasdansleZooException e){
            System.out.println("Le loup n'est pas dans le zoo ");
        }catch(NestpasBlesseException e){
            System.out.println("Le loup n'est pas bléssé");
        }
        try{
            zoo.soigner(toucan);
            System.out.println("le toucan a bien été soigné");
        }catch(NestpasBlesseException e){
            System.out.println("Le toucan n'est pas bléssé");
        }catch(NestpasdansleZooException e){
            System.out.println("Le toucan n'est pas dans le zoo");
        }
    }
}
