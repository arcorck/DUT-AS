<?php
// base du modele : la connexion à la BD
require("connect.php");
function connect_db()
{
    $dsn="mysql:dbname=".BASE.";host=".SERVER;
    try{
      $connexion=new PDO($dsn,USER,PASSWD);
    }
    catch(PDOException $e){
      printf("Échec de la connexion : %s\n", $e->getMessage());
      exit();
    }
    return $connexion;
}

function get_all_films(){
  //require("connect.php"=;
  $connexion = connect_db();
  $sql= "SELECT * from films JOIN individus on individus.code_indiv=films.realisateur";
  if(!$connexion->query($sql))
  echo "Pb";
  else{
    $films = Array();
    foreach ($connexion-> query($sql) as $row)
     $films[] = $row;
  }
  return $films;
}

 ?>
