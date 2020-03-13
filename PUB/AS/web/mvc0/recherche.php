<html>
<head>
<title>
Recherche dans une table MySQL avec PDO
</title>
<meta charset="utf-8">
</head>
<body>
<?php $wanted=$_GET['ID']; 
if (!empty($wanted)){
	echo "<h1>Recherche de  $wanted </h1>";
	require_once('modele.php');
	$connexion=connect_db();
	$sql="SELECT * from CARNET where ID='".$wanted."'";
	if(!$connexion->query($sql))
		echo "Pb de requete";
	else{
	foreach ($connexion->query($sql) as $row)
		echo $row['NOM']." ".$row['PRENOM']."</br>\n";
  }
}
  ?>
</body>
</html>
