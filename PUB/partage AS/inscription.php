<pre>
<?php
require_once("connection.php");

print_r($_POST);
if (empty($_POST["pseudo"]) || empty($_POST["password"]) || empty($_POST["persopref"])){
echo 'oui';

}else{

$pseudo=$_POST["pseudo"];
$password=$_POST["password"];
$persopref=$_POST["persopref"];

$requeteSQL=$connection->prepare("SELECT Pseudo from user where Pseudo=:Pseudo");
$requeteSQL->bindParam(':Pseudo',$pseudo, PDO::PARAM_STR);
$requeteSQL->execute();
$listepseudo=$requeteSQL->fetchAll();
echo count($listepseudo);
if (count($listepseudo)==0){
  $requeteInscription=$connection->prepare("INSERT into user values (:pseudo, :password, :persopref)");
}
else{
  echo 'pseudo existe déjà';
}


}
?>
</pre>
