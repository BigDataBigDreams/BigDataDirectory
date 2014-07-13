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

function checkValidBrand($connectDB, $tableName, $brand)
{
	echo "Hello";
	$sql = "SELECT DISTINCT brand FROM $tableName WHERE brand LIKE '$brand'";
	$result = mysqli_query($connectDB, $sql);
	$row_cnt = $result->num_rows;
	echo $row_cnt;
}

// $connect = connectDB($config);
// closeDB($connect);
?>