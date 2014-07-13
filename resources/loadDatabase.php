<?php
// echo $config['db']['govhack']['dbname'] . " " . $config['db']['govhack']['username']
//  . " " . $config['db']['govhack']['password']
//  . " " . $config['db']['govhack']['host'];

function connectDB($config)
{
	$connectDB = mysqli_connect($config['db']['govhack']['host'],$config['db']['govhack']['username'],
		$config['db']['govhack']['password'],$config['db']['govhack']['dbname']);

	//Check connection
	if (mysqli_connect_errno())
	  echo "Failed to connect to MySQL: " . mysqli_connect_error() . "<br>";

	// else
	// 	echo "Success load database" . "<br>";

	return $connectDB;
}

function closeDB($connect)
{
	mysqli_close($connect);
	// echo "Closed database";
}



?>