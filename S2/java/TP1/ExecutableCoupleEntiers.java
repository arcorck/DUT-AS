public class ExecutableCoupleEntiers {

    public static void main(String [] args) {
        CoupleEntiers couple = new CoupleEntiers(1, 5);
        couple.setPrem(-16);
        System.out.println(couple.toString()); // (1)
        System.out.println(couple.fraction()); // (2)
        couple.setSec(-6);
        System.out.println(couple.getPrem()+" "+couple.getSec());
        System.out.println(couple.somme()); // affiche -22
        System.out.println(couple.toString());
        CoupleEntiers c = new CoupleEntiers (16,6);
        System.out.println(c.toString());
        System.out.print("Addition des deux couples : ");
        System.out.println(couple.plus(c).toString());
    }
}