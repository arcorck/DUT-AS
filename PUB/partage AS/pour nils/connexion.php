
<pre>
<?php
  require_once('connexion_bdd.php');

  if(!empty($_POST['envoyer'])) //si name n'est pas vide
  {
    !empty($_POST['nom']) ? $nom = $_POST['nom'] : $nom = NULL; // si sinon la valeur name n'est pas vide on récupere les donnee
    !empty($_POST['prenom']) ? $prenom = $_POST['prenom'] : $prenom = NULL;
    !empty($_POST['mdp']) ? $mdp = $_POST['mdp'] : $mdp = NULL;
    !empty($_POST['pseudo']) ? $pseudo = $_POST['pseudo'] : $pseudo = NULL; // NULL : variable vide, equivalent du none
  }


//si un des champs n'est pas rempli, on redirige l'utilisateur

if(empty($mdp) or empty($nom) or empty($pseudo) or empty($prenom))
{
  header('Location:../index.php');
  exit(0);
}

//si tous les champs remplis

$select = $connexion -> prepare("SELECT * FROM user WHERE nom = :nom and mdp = :mdp and pseudo = :pseudo and prenom = :prenom");

$select -> bindParam(':nom', $nom, PDO::PARAM_STR); // lier le php a la requete
$select -> bindParam(':prenom', $prenom, PDO::PARAM_STR);
$select -> bindParam(':mdp', $mdp, PDO::PARAM_STR);
$select -> bindParam(':pseudo', $pseudo, PDO::PARAM_STR);

$select -> execute();
$compte = $select -> fetch();

print_r($compte);

 ?>
</pre>
