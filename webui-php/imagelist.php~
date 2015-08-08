<?php
include('config.php');
$root_dir=$_SERVER['DOCUMENT_ROOT'].$data;
  
$book = $_POST["book"]; 
$dir=$root_dir.$books_dir;//contains the json files
$bookpath=$dir.$book;//path to selected "json file" from the lists
$str_data=file_get_contents($bookpath);//read the .json format from the selected json file
$data = json_decode($str_data,true);
$len= count($data["book"]["images"]);//count the number of images in the json file
for ($i=0;$i<$len;$i++)
{
echo $data["book"]["images"][$i]."|";   //retrive all images with their path 
}
?>
