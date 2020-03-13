<?php
require('connexion.php');

$connexion = connect_bd();

$sql = "SELECT * from CARNET";
$data = $connexion->query($sql);
while($row = $data->fetch())
	echo $row['PRENOM'].' '.$row['NOM'].'<br/>\n';


