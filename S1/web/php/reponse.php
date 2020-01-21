<!doctype html>
<html>
<head>
<meta charset="utf-8" />
<title>
Test Formulaire PHP
</title>
</head>
<body>
<h1>Bonjour,  <?php echo $_GET['nom'] ?></h1>
<h2>Vous avez  <?php echo $_GET['age']?> ans</h2>
<?php if (($_GET['age']>"0") and ($_GET['age']<"120"))
        echo "Votre âge semble bien valide"; ?>
    <br><br>
   <?php
    $n = $_GET['nom'];
    $a = $_GET['age'];
    ?>
Votre nom est stocké dans la variable $n
dont le type est <?php echo gettype($n) ?>

Votre âge est stocké dans la variable <b>$a</b>
<br/> dont le type est <i><?php echo gettype($a); ?></i>
<br/> On peut la transformer en <i>integer</i> en faisant : settype($a,"integer")
   <?php settype($a,"integer"); ?> <br>
    Type de $a :<?php echo gettype($a); ?>
</body>

</html>
