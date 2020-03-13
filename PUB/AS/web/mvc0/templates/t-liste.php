<?php 
	$title = "Liste des amis";
	// on démarre la bufférisation
	ob_start();
?>
	<ul>
	<?php foreach ($amis as $ami): ?>
			<li>
				<a href="recherche.php?ID=<?php echo $ami['ID']; ?>" >
					<?php echo $ami['NOM']; ?>
				</a>
			</li>
		<?php endforeach; ?>
	</ul>
	<?php 
	// on récupère la variable content 
	// tout ce qui a été bufferisé
	// et on nettoie le buffer
	$content = ob_get_clean(); 
	include 'baseLayout.php';
	?>
