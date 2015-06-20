 <?php $book = $_POST["book"]; 
  $dir="visual-search/indexedbooks/";
  $bookpath=$dir.$book;
  
  $splitstr=split(".json",$book);
  $jsonresultfile=$splitstr[0]."-result.json";
 
  $callimgseg= exec("python python/mainimgsegmenter.py -j $bookpath -b $jsonresultfile");
  echo $callimgseg;
  
  //echo $dir.$book;

?>




