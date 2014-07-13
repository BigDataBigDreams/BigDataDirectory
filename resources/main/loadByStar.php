<?php

include "../loadFiles.php";

$connectDB = mysqli_connect($config['db']['govhack']['host'],$config['db']['govhack']['username'],
		$config['db']['govhack']['password'],$config['db']['govhack']['dbname']);

//Check connection
if (mysqli_connect_errno())
  echo "Failed to connect to MySQL: " . mysqli_connect_error() . "<br>";

$data = array();

$_POST['tableName'] = "airconditioner";
$_POST['brand'] = "AKAI";
$_POST['star'] = 2;

if( isset($_POST['tableName']) && !empty($_POST['tableName']) 
	&& isset($_POST['brand']) && isset($_POST['star']) )
{
	try
	{
		$tableName = $_POST['tableName']; 
		$brand = strtoupper($_POST['brand']);
		$star = $_POST['star'];
		$max = $star + 0.5; $min = $star - 0.5; 
		$sql = "SELECT * FROM airconditioner 
				WHERE UPPER(brand) LIKE 'AKAI' 
				AND star BETWEEN $min AND $max 
				ORDER BY brand ASC limit 10";
		$result = mysqli_query($connectDB, $sql);
		if($result)
		{
			while($row = mysqli_fetch_array($result))
			{	
		    	$data[] = array(
			        "id" => $row['id'],
			        "brand" => $row['brand'],
			        "model" => $row['model'],
			        "power" => $row['power'],
			        "star" => $row['star'],
				);
			}
		}
	}
	catch (Expcetion $e)
	{
		$data = array();
		$data[] = newEmptyModelsArray();
	}
}
else
{
	$data[] = newEmptyModelsArray();
}



echo json_encode($data);

mysqli_close($connectDB);
?>