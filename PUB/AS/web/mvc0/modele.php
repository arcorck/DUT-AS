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

function get_all_friends()
{
    $connexion=connect_db();
	  $sql="SELECT * from CARNET";
	  $data=$connexion->query($sql);
	  $amis=Array();
	  while($row=$data->fetch())
		    $amis[]=$row;
	  return $amis;
}


