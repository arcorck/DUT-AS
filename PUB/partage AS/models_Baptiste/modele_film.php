<?php
require("connect.php");

class Film{
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

    function get_all_film(){
        $sql=self::$connexion->prepare("SELECT * from films");
        $sql->execute();
        $films=$sql->fetch(PDO::FETCH_OBJ);

        return $films;
    }

    function get_film_by_id($id){
        $sql=self::$connexion->prepare("SELECT * from films WHERE code_film=:code_film");
        $sql -> bindParam(":code_film",$id,PDO::PARAM_INT);
        $sql -> execute();
        $film = $sql->fetch(PDO::FETCH_OBJ);
    }

    function add_film($film){
        $req=self::$connexion-> prepare("INSERT INTO films(titre_original,titre_francais,pays,date,duree,realisateur) values (:titreO,:titreF,:pays,:date,:duree,:real)");
        $req-> bindParam(":titreO",$film->titre_original,PDO::PARAM_STR);
        $req-> bindParam(":titreF",$film->titre_francais,PDO::PARAM_STR);
        $req-> bindParam(":pays",$film->pays,PDO::PARAM_STR);
        $req-> bindParam(":date",$film->date,PDO::PARAM_INT);
        $req-> bindParam(":duree",$film->duree,PDO::PARAM_INT);
        $req-> bindParam(":real",$film->realisateur,PDO::PARAM_STR);
        return $req->execute();
    }

    function delete_film($id){
        $sql=self::$connexion->prepare("DELETE from films where code_film=:id");
        $sql->bindParam(":id",$id,PDO::PARAM_INT);
        return $sql->execute();
    }

    function update_film($film){
        $req=self::$connexion->prepare("UPDATE films set titre_original=:titreO, titre_francais=:titreF, pays=:pays, date=:date, duree=:duree, realisateur=:real where code_film=:id");
        $req -> bindParam("titreO",$film->titre_original,PDO::PARAM_INT);
        $req-> bindParam(":titreF",$film->titre_francais,PDO::PARAM_STR);
        $req-> bindParam(":pays",$film->pays,PDO::PARAM_STR);
        $req-> bindParam(":date",$film->date,PDO::PARAM_INT);
        $req-> bindParam(":duree",$film->duree,PDO::PARAM_INT);
        $req-> bindParam(":real",$film->realisateur,PDO::PARAM_STR);
        return $req->execute();
    }

}