<html>
<head>
<title>
visual Search
</title>

</head>
<body>
<?php  ?>

<p><div style="text-align:left;color:blue;font-size:25px;">Images available..</div></p>

<table>
<tr>

<td>
<!--<p><div style="text-align:left;color:blue;font-size:25px;">Images available..</div></p>-->
  <form align ="left"  action="<?php $_PHP_SELF ?>" method="GET">
  <select  style="width: 400px;" size="18" name="imagelist[]" multiple>
<?php

  $images = array();
        $dir = "visual-search/images/user-upload/"; 
        
       // OPEN THE DIRECTORY
        $dirHandle = opendir($dir); 
        // LOOP OVER ALL OF THE FILES
        $StringSent=urlencode($dir);
        while ($file = readdir($dirHandle)) { 
         // IF IT IS NOT A FOLDER, AND ONLY IF IT IS A .JPG WE ACCESS IT
         // if(!is_dir($file) && (strpos($file, '.jpg')||strpos($file, '.png'))>0) {
      if(!is_dir($file) && (strpos($file, '.jpg')||strpos($file,'.png'))>0) {
           //echo "$file"."<br />";
           $images[]=$file;     
           }

         }
         
         $array_length = count($images);
         //echo "$array_length";
         
         for ($i=0;$i<$array_length;$i++)
         {
          ?>
         <option value="<?=$images[$i];?>"><?=$images[$i];?></option>
         <?php
         
         }
                 
         closedir($dirHandle);
         ?>
                   
</select><br>
<input type="submit"  style= "font-size: 28px; color: red;" name="submit" value="view" >
</form>
</td>


<td>
<form>
<?php

  foreach ($_GET['imagelist'] as $names)
         {
        // print "Selected image:$names<br/>";
         ?>

         <img src = <?php echo $dir.$names ?>  height="350" width="400">
         <br>
         <?php
          echo "Selected image is:".$names;
         
         }

?>
</form>
</td>

</tr>
</table>

<p><div style="text-align:left;color:blue;font-size:25px;">Template images available..</div></p>
<table>
<tr>
<td>
<form align ="left"  action="<?php $_PHP_SELF ?>" method="GET">
  <select  style="width: 400px;" size="18" name="tempimagelist[]" multiple>
<?php

  $tempimages = array();
        $tempdir = "visual-search/images/template-images/";

       // OPEN THE DIRECTORY
        $tempdirHandle = opendir($tempdir);
        // LOOP OVER ALL OF THE FILES
        $tempStringSent=urlencode($dir);
        while ($tempfile = readdir($tempdirHandle)) {
         if(!is_dir($tempfile) && (strpos($tempfile, '.jpg')||strpos($tempfile, '.png'))>0) {
           //echo "$file"."<br />";
           $tempimages[]=$tempfile;
           }

         }

         $temparray_length = count($tempimages);
         //echo "$array_length";

         for ($i=0;$i<$temparray_length;$i++)
         {
          ?>
         <option value="<?=$tempimages[$i];?>"><?=$tempimages[$i];?></option>
         <?php

         }

         closedir($tempdirHandle);
         ?>
      </select><br>
<input type="submit"  style= "font-size: 28px; color: red;" name="submit" value="view" >
</td>
</form>

<td>
<form>
<?php

  foreach ($_GET['tempimagelist'] as $names)
         {
        
         ?>

         <img src = <?php echo $tempdir.$names ?>  height="100" width="100">
         <br>
         <?php
          echo "Selected template image is:".$names;

         }

?>
</form>
</td>
</tr>
</table>
<br>
<form name="form" action="matchtemplate.php" method="POST"
enctype="multipart/form-data">

<?php

  foreach ($_GET['imagelist'] as $names)
{
//echo "hello".$names;
  session_start();
  $_SESSION['srcimg'] =$names;
}

foreach ($_GET['tempimagelist'] as $names)
{
//echo "hello".$names;
  session_start();
  $_SESSION['tempimg'] =$names;
} 
?>

<input type="submit"  style= "font-size: 28px; color: red;" name="submit" value="Search" >
</form>

</body>
</html>
