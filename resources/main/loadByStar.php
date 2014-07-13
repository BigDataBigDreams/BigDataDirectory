<?php

include "../loadFiles.php";

$connectDB = mysqli_connect($config['db']['govhack']['host'],$config['db']['govhack']['username'],
		$config['db']['govhack']['password'],$config['db']['govhack']['dbname']);

//Check connection
if (mysqli_connect_errno())
  echo "Failed to connect to MySQL: " . mysqli_connect_error() . "<br>";

$data = array();

if( isset($_POST['tableName']) && !empty($_POST['tableName']) && isset($_POST['star']) )
{
	try
	{
		$tableName = $_POST['tableName']; 
		$star = $_POST['star'];
		$sql = "SELECT * FROM $tableName ORDER BY ABS(star-$star) limit 10;";
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
		//$data = array();
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