<!doctype html>
<html>
<head>
<title>
Recherche une personne par son nom:
</title>
<body>
<h1>
Details sur la personne:
</h1>

<?php
//require("connexion.php");
//$connexion = connect_bd();
require("connect.php");
$dsn="mysql:dbname=".BASE.";host=".SERVER;
    try{
      $connexion=new PDO($dsn,USER,PASSWD);
    }
    catch(PDOException $e){
      printf("Échec de la connexion : %s\n", $e->getMessage());
      exit();
    }

$sql = "SELECT * from CARNET where ID=:id";
// on prépare la requête
$stmt = $connexion->prepare($sql);
// on associe le ? avec la valeur passée par GET sur l'URL
$stmt->bindparam(':id',$_GET['ID']);
// on exécute la requête
$stmt->execute();
// on récupère le résultat sous forme d'objet
if ($pers = $stmt->fetch(PDO::FETCH_OBJ))
  { 
    echo $pers->NOM."<br/>\n";
    echo $pers->PRENOM."<br/>\n";
    echo $pers->NAISSANCE."<br/>\n";
    echo $pers->VILLE."<br/>\n";
  }
else echo "Personne inconnue !";
?>
</body>
</html>

