	<!DOCTYPE html>
	<html>
	<head>
		<title>Clasificador de textos ODS</title>
		<link rel="stylesheet" type="text/css" href="css/style.css">
		<link rel="icon" href="images/favicon.ico" type="image/ico" />
	</head>
	<body>
	<header id="primario">
	<div class="contenedor">
		<h1>Modelo de Tópicos basado en los Objetivos de desarrollo sostenible
		</h1>
	</div>

	</header>
	<nav id="navbar">
	<div class="contenedor">
		<ul>
			<li><a href="#">HOME</a></li>
			<li><a href="#">ABOUT</a></li>
			<li><a href="#">CONTACT US</a></li>
		</ul>
	</div>

	</nav>
	<section id="showcase">
		´<div class="contenedor">
			

		</div>
	</section>
	<div class="contenedor2">
	<section id="main">
		<h1>BIENVENIDO</h1>
		<p>Este proyecto  
		se basa en tecnologías de Inteligencia Artificial y Machine Learning para crear un modelo que sea capaz de obtener el ODS relacionado con un texto dado. 
		<br>
		Para probar el modelo, introduzca el texto a clasificar en el recuadro inferior y pulse enviar. El resultado será una lista en la que se muestra la probabilidad de que el texto corresponda a cada uno de los ODS. 
		<br>
		La respuesta incluye una lista con todos los ODS, junto con un porcentaje que indica la probabilidad de pertencia a la clase</p>
	
	</section>
	<aside id="sidebar">
		
	</aside>
	</div>
	<div class="contenedor3">
	<section id="main">
		<h1>¡PRUÉBELO!</h1>
		<form action="Web_ODS.php" method="get">
 <textarea rows="5" cols="60" name="texto_a_clasificar" placeholder="Introducir texto"></textarea>

    <input type="submit">
</form>
<br>
<?php 
file_put_contents("texto.txt", $_GET["texto_a_clasificar"]);
$output = shell_exec("python import_requests.py");
echo "<pre>". $output."</pre>";



?> 
	</section>
	
	</div>
	<footer id= "pie">
	<p> <b>Developed by Julen Pérez Álvarez, 
		in colaboration with Oscar Corcho and Carlos Badenes-Olmedo
		Model developed by María del Carmen Rodríguez García
		</b></p>
		
		<p><b>Copyright &copy;2021 SDGs Topic Model Classifier</b></p>
	</footer>
	</body>
	</html>