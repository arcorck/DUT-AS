<?php
// c-list.php : controleur de liste 
// qui appelle le modèle, récupère des données
// et les renvoie au template
	require_once 'modele.php';
	$amis = get_all_friends();
	require 'templates/t-liste.php';

