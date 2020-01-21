<html>
<head>
<title>
Connexion à MySQL avec PDO
</title>
<meta charset="utf-8">
</head>
<body>
<h1>
Interrogation de la table CARNET avec PDO
</h1>

<?php

require("connect.php");
// pour oracle: $dsn="oci:dbname=//serveur:1521/base
// pour sqlite: $dsn="sqlite:/tmp/base.sqlite"
$dsn="mysql:dbname=".BASE.";host=".SERVER;
    try{
      $connexion=new PDO($dsn,USER,PASSWD);
      echo("connexion reussie");
    }
    catch(PDOException $e){
      printf("Échec de la connexion : %s\n", $e->getMessage());
      exit();
    }
$sql="SELECT * from CARNET";
if(!$connexion->query($sql)) echo "Pb d'accès au CARNET";
else{
    echo "<table><tr><td>Nom</td><td>Prenom</td></tr>";
    foreach ($connexion->query($sql) as $row)
        echo "<tr><td>".$row['NOM'].
          "<td>".$row['PRENOM']."</td></tr>";
echo "</table>";
}

?>

<form action="carnet_z.php" method="post">
<input type="text" name="champ_recherche" placeholder="commence par : ">
<input type="submit" name="search" value="rechercher">
</form>
</body>
</html>