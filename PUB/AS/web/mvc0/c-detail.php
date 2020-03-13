<?php
// c-list.php : controleur de détail
// qui appelle le modèle, récupère des données
// et les renvoie au template
// attend un paramètre ID passé en GET
	require_once 'modele.php';
	$pers = get_friend_by_id($_GET['ID']);
	require 'templates/t-detail.php';

