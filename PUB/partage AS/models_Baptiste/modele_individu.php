<?php
require("connect.php");

class Individu{
    private static $connexion;

    function __construct(){
        $dsn="mysql :dbname=".BASE.";host=".SERVER;
        try{
            self::$connexion=new PDO($dsn,USER,PASSWD);
        }
        catch(PDOException $e){
            printf("Echec de la connexion : $s\n", $e->getMessage());
            $this->connexion=NULL;
        }
    }
    function get_all_individu(){
        $sql=self::$connexion->prepare("SELECT * from individus");
        $sql->execute();
        $films=$sql->fetch(PDO::FETCH_OBJ);

        return $films;
    }

    function get_individu_by_id($id){
        $sql=self::$connexion->prepare("SELECT * from individus WHERE code_indiv=:code_indiv");
        $sql -> bindParam(":code_indiv",$id,PDO::PARAM_INT);
        $sql -> execute();
        $film = $sql->fetch(PDO::FETCH_OBJ);
    }

    function add_individu($individu){
        $req=self::$connexion-> prepare("INSERT INTO individus(nom,prenom,nationalite,date_naiss,date_mort) values (:nom,:prenom,:pays,:dateN,:dateM)");
        $req-> bindParam(":nom",$individu->nom,PDO::PARAM_STR);
        $req-> bindParam(":prenom",$individu->prenom,PDO::PARAM_STR);
        $req-> bindParam(":pays",$individu->nationalite,PDO::PARAM_STR);
        $req-> bindParam(":dateN",$individu->date_naiss,PDO::PARAM_STR);
        $req-> bindParam(":dateM",$individu->date_mort,PDO::PARAM_STR);
        $req->execute();
    }

    function delete_individus($id){
        $sql=self::$connexion->prepare("DELETE from individus where code_indiv=:id");
        $sql->bindParam(":id",$id,PDO::PARAM_INT);
        $sql->execute();
    }

    function update_individus($individu){
        $req=self::$connexion-> prepare("UPDATE individus(nom=:nom,prenom=prenom,nationalite=pays,date_naiss=dateN,date_mort=dateM where code_indiv=:id");
        $req-> bindParam(":nom",$individu->nom,PDO::PARAM_STR);
        $req-> bindParam(":prenom",$individu->prenom,PDO::PARAM_STR);
        $req-> bindParam(":pays",$individu->nationalite,PDO::PARAM_STR);
        $req-> bindParam(":dateN",$individu->date_naiss,PDO::PARAM_STR);
        $req-> bindParam(":dateM",$individu->date_mort,PDO::PARAM_STR);
        $sql->bindParam(":id",$individu->code_indiv,PDO::PARAM_INT);
        $req->execute();
    }
}
