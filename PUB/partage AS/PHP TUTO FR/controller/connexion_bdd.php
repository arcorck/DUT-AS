<?php

$server = 'servinfo-mariadb';
$user = 'meunier';
$mdp = 'meunier';
$base = 'DBmeunier';

try
{
    $connexion = new PDO("mysql:host=$server;dbname=$base", $user, $mdp);

    $connexion -> setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    echo '<script>console.log("connexion reussie")</script>';
}
catch(PDOException $msg)
{
    echo '<h1>CONNEXION FAILED</h1>';
}

?>