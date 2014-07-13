<?php
include 'config.php';
include 'loadDatabase.php';

function newEmptyArray()
{
	return $newEmptyArray = array(
    "db" => array(
	        "id" => "1",
	        "brand" => "",
	        "model" => "",
	        "power" => "",
	        "star" => "",
	    ),
	);
}

// $connect = connectDB($config);
// closeDB($connect);
?>