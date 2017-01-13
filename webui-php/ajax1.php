 <?php 
 include('config.php');
  $root_dir=$_SERVER['DOCUMENT_ROOT'].$data;
  
  $imagefile = $_POST["imagefile"];
  $segmentimage = $_POST["segmentimage"];
 
   $abs_jsonpath= exec("python python-scripts/mainimgsegmenter.py -i $imagefile -b $segmentimage -d $root_dir");
   $rel_jsonpath=str_replace($_SERVER['DOCUMENT_ROOT'],"",$abs_jsonpath);
 
   echo $rel_jsonpath;
   
?>


