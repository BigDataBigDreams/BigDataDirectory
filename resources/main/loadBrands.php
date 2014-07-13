<?php

include "../loadFiles.php";

$connect = connectDB($config);

$data = "";

if( isset($_POST['tableName']) && !empty($_POST['tableName'] && isset($_POST['brand']))
{

}
else
{

}

echo $data;
//echo json_encode($data);

closeDB($connect);
?>