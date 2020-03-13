<?php
include 'vendor/autoload.php';

// on inclus le modele
include 'models/modele_film.php';

try {

  // indiquer le dossier ou on trouve les templates
  $loader = new Twig\Loader\FilesystemLoader('templates');
  //initialiser l'environnement Twig_Loader_Filesystem
  $twig = new Twig\Environment($loader);


  // Récupérer les données depuis la base
  $films = get_all_films();
  // Charger le templates
  $template = $twig->load('films1.html');

  $titre = "Liste des films du carnet trié par titre";
  echo $template->render(array(
    'titre' => $titre,
    'films' => $films,
  ));
} catch (Exception $e) {
  die ('ERROR: ' . $e->getMessage());
}
 ?>
