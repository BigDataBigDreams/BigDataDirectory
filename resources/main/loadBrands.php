<?php

include "../loadFiles.php";

$connectDB = mysqli_connect($config['db']['govhack']['host'],$config['db']['govhack']['username'],
		$config['db']['govhack']['password'],$config['db']['govhack']['dbname']);

//Check connection
if (mysqli_connect_errno())
  echo "Failed to connect to MySQL: " . mysqli_connect_error() . "<br>";

$data = array();

if( isset($_POST['tableName']) && !empty($_POST['tableName']) && isset($_POST['brand']) )
{
	$tableName = $_POST['tableName']; $brand = strtoupper($_POST['brand']);
	$sql = "SELECT DISTINCT brand FROM $tableName WHERE UPPER(brand) LIKE '$brand%' limit 10;";
	$result = mysqli_query($connectDB, $sql);
	if($result)
	{
		while($row = mysqli_fetch_array($result))
		{
	    	$data[] = $row[0];
		}
	}
} else {
	$data = 'invalid state';	
}

echo json_encode($data);

mysqli_close($connectDB);
?>