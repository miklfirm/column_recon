<!DOCTYPE html>
<html>
<head>
<title>Поиск совпадений в двух списках онлайн: excel, txt | WonderBrains.pro Tools</title>
<meta charset="utf-8" />
</head>
<body>
        <form action="/" enctype="multipart/form-data" method="post">
		<label for="cheese">Выберете файл в котром будем <b>искать совпадения</b></label><br>
	    <input type="file" name="original_list"><br><br>
		<label for="cheese">Выберете файл из котрого будем брать <b>слова поиска</b></label><br>
		<input type="file" name="search_list"><br><br>
        <input type="submit" value="Найти">
        </form>

<?php
if ($_FILES){
	if (($_FILES["original_list"]["error"]== UPLOAD_ERR_OK))
	{
		$hash_name_original = substr(hash('sha256', openssl_random_pseudo_bytes(20)),-16);
		$hash_name_search = substr(hash('sha256', openssl_random_pseudo_bytes(20)),-16);
		$hash_name_output = substr(hash('sha256', openssl_random_pseudo_bytes(20)),-16);


		$path_original_list = __DIR__ . "/uploads/". $hash_name_original . "_".$_FILES["original_list"]["name"];
		$path_search_list = __DIR__ . "/uploads/". $hash_name_search . "_".$_FILES["search_list"]["name"];
		$path_output_list = __DIR__."/uploads/".$hash_name_output."_output.txt";

		move_uploaded_file($_FILES["original_list"]["tmp_name"], $path_original_list);
		move_uploaded_file($_FILES["search_list"]["tmp_name"], $path_search_list);
		//print_r($_FILES);
		echo "<br />Файлы загружен в ".$path_original_list;
		echo "<br />Файлы загружен в ".$path_search_list;

		echo shell_exec ('python3 ' . __DIR__ . '/script.py ' . $path_original_list . ' ' . $path_search_list . ' ' . $path_output_list);
		echo "<br />python done";
		echo "<br />";
		echo "<a href='/uploads/".$hash_name_output."_output.txt' target='_blank' download=''>download result</a>";
	}else {
		echo "<br />Error 1: ".$_FILES["original_list"]["error"];
		echo "<br />Error 2: ".$_FILES["search_list"]["error"];
	}
	}
?>

</body>
</html>