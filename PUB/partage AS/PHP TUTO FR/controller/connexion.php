<pre>
<?php
require_once('connexion_bdd.php');

if(!empty($_POST['envoyer']))
{
    !empty($_POST['nom']) ? $nom = $_POST['nom'] : $nom = NULL;
    !empty($_POST['mdp']) ? $mdp = $_POST['mdp'] : $mdp = NULL;
    !empty($_POST['pseudo']) ? $pseudo = $_POST['pseudo'] : $pseudo = NULL;
}

if(empty($mdp) || empty($pseudo) || empty($nom))
{
    header('Location:../index.php');
    exit(0);
}

$select = $connexion -> prepare("SELECT * FROM lesuser WHERE pseudo = :pseudo and mdp = :mdp");
$select -> bindParam(':pseudo', $pseudo, PDO::PARAM_STR);
$select -> bindParam(':mdp', $mdp, PDO::PARAM_STR);

$select -> execute();
$compte = $select -> fetch(PDO::FETCH_ASSOC);

print_r($compte);


?>
</pre>