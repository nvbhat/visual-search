<html>
<head>
<title>
Visual Search Results
</title>
</head>
<body>
<?php 

session_start();
$srcimg=$_SESSION['srcimg'];
$tempimg=$_SESSION['tempimg'];
//echo $srcimg;
//echo $tempimg;

$ext = substr($srcimg, strrpos($srcimg, '.') + 1);

 if ($ext == "jpg")
 {
  $splitstr=split(".jpg",$srcimg);
   $resultimg=$splitstr[0]."-result.jpg";
   $jsonresultfile=$splitstr[0]."-result.json";
 
    $outimgpathjpg="visual-search/images/searched-images/";

  exec("./imgsearch visual-search/images/user-upload/$srcimg visual-search/images/template-images/$tempimg visual-search/books/searched-books/$jsonresultfile visual-search/images/searched-images/$resultimg");
 

?>

 <img src = <?php echo $outimgpathjpg.$resultimg ?>  height="500" width="500">

<?php 
}


if($ext == "png")
{ 

$splitstr=split(".png",$srcimg);
   $resultimg=$splitstr[0]."-result.png";
   $jsonresultfile=$splitstr[0]."-result.json";
  $outimgpathpng="visual-search/images/searched-images/";

   exec("./imgsearch visual-search/images/user-upload/$srcimg visual-search/images/template-images/$tempimg visual-search/books/searched-books/$jsonresultfile visual-search/images/searched-images/$resultimg");
  //echo " png";
?>
 <img src = <?php echo $outimgpathpng.$resultimg ?>  height="500" width="500">

<?php
}

?>
</body>
<html>
