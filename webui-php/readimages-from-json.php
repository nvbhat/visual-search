<?php
error_reporting(0);
$book = $_POST['book']; 
$dir="visual-search/indexedbooks/";//contains the json files
$bookpath=$dir.$book;//path to selected "json file" from the lists

$str_data = file_get_contents($bookpath);//read the .json format from the selected json file
$data = json_decode($str_data,true);

$len= count($data["book"]["images"]);

if($len == 0){
	echo '<br ><br ><br ><br ><br ><br ><br ><br ><br ><br ><br ><br ><center><h1>No images found in the json file : '.$book.'</h1></center>';
}else{
echo '<ul class="thumbnails">';
for ($i=0;$i<$len;$i++)
{
 echo '<li>';
 echo '<a  href="example-images/'.$data["book"]["images"][$i].'" data-standard = "visual-search/images/'.$data["book"]["images"][$i].'"><img src="visual-search/images/'.$data["book"]["images"][$i].'" alt="" onClick = "getName(this.src)" height = "120px" width = "140px" /></a><br>';
echo $data["book"]["images"][$i];
echo '</li>';
} 
echo '</ul>';
}
?>
