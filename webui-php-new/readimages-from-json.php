<?php

$book = $_POST["book"]; 
$dir="visual-search/indexedbooks/";
$bookpath=$dir.$book;
$str_data=file_get_contents($bookpath);//read the .json format from book.json file
$data = json_decode($str_data,true);

$len= count($data["book"]["images"]);

for ($i=0;$i<$len;$i++)
{
echo $data["book"]["images"][$i]."|";
}
?>
