<!doctype html>
<html>
<head>
<meta charset="utf-8" />
<title> Bonjour depuis PHP </title>
</head>
<body>
<?php echo 'Bonjour généré dynamiquement en PHP !'; 
phpinfo();
echo $_SERVER['HTTP_USER_AGENT']; ?>
</body>
</html>