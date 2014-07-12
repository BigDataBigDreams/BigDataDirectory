<!DOCTYPE html>

<html>
<head>
	<title>File uploading</title>
</head>

<body>
	<h1>Admin page</h1>
	<form action="upload.php" method="post" enctype="multipart/form-data">
	<label for="file">Filename:</label>
	<input type="file" name="file" id="file"><br>
	<input type="submit" name="submit" value="Submit">
</body>

</html>
