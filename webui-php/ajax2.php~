 <?php 
  include('config.php');
  $root_dir=$_SERVER['DOCUMENT_ROOT'].$data;

  $imagefile = $_POST["imagefile"]; //image file like "example-images/imagename.jpg"
  $segmentimage = $_POST["segmentimage"];//segmented book-name like "imagename-result.json"
  
 //$abs_jsonpath= exec("python python-scripts/wordsegment.py -i $imagefile -b $segmentimage"); //old algorithm ("wordsegment.py") for manuscripts images
  
   $abs_jsonpath= exec("python python-scripts/segword_manuscript.py -i $imagefile -b $segmentimage -d $root_dir");//updated algorithm (segword_manuscript.py)
   $rel_jsonpath=str_replace($_SERVER['DOCUMENT_ROOT'],"",$abs_jsonpath);
  echo $rel_jsonpath;
 

?>




