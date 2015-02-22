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
  <form align ="left" method="post" action="Rect-Template/demos/crop.php">
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

</tr>
</table>  

</body>
</html>

