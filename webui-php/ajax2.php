 <?php 
  $imagefile = $_POST["imagefile"]; //image file like "example-images/imagename.jpg"
  $segmentimage = $_POST["segmentimage"];//segmented book-name like "imagename-result.json"
  
    //$callimgseg= exec("python python-scripts/wordsegment.py -i $imagefile -b $segmentimage"); //old algorithm ("wordsegment.py") for manuscripts images
  
  $callimgseg= exec("python python-scripts/segword_manuscript.py -i $imagefile -b $segmentimage");//updated algorithm (segword_manuscript.py)
 
  echo $callimgseg;
 

?>




