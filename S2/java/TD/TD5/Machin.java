//ERREUR !!
class Machin{
    int renvoie5(){
        return 5;
    }
    static int chose(){
        return renvoie5();
    }
}


//PAS D'ERREUR !!
class Machin{
    static int renvoie5(){
        return 5;
    }
    int chose(){
        return renvoie5();
    }
}