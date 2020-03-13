<?php
require("connect.php");
$dsn = "mysql:dbname=".BASE.";host=".SERVER;
    try{
      $connexion = new PDO($dsn,USER,PASSWD);
    }
    catch(PDOException $e){
      printf("Échec de la connexion : %s\n", $e->getMessage());
      exit();
    }
$sql = "SELECT * from CARNET";
$data = $connexion->query($sql);
$amis = Array();
while($row=$data->fetch())
	$amis[]=$row;
// on a remplit correctement le tableau $amis
// et on le passe au template listeamis.php
// qui va s'occuper de l'affichage
require "templates/listeamis.php";


