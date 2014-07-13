<?php
include 'config.php';

function newEmptyModelsArray()
{
	return $newEmptyArray = array(
    array(
	        "id" => "1",
	        "brand" => "",
	        "model" => "",
	        "power" => "",
	        "star" => "",
	    ),
	);
}

function checkValidBrand($connectDB, $brand)
{
	$sql = "SELECT DISTINCT brand FROM $tableName WHERE brand LIKE '$brand%'";
	$result = mysqli_query($connectDB, $sql);
}

// $connect = connectDB($config);
// closeDB($connect);
?>