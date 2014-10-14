<html>
 <head>
   <title>Listing Images</title>
    </head>
     <body>
    <p><div style="text-align:center;color:blue;font-size:20px;">select images from the lists</div></p>
  <form align ="center" method="post" action="viewbook.php">
    <select  style="width: 400px;" size="18" name="dynamic_data[]" multiple>
    <!--<select name="images[]" multiple>-->
      <?php 
      // SPECIFY THE DIRECTORY                                                                                         
        $images = array();
        $dir = "visual-search/images/"; 
        
       // OPEN THE DIRECTORY
        $dirHandle = opendir($dir); 
        // LOOP OVER ALL OF THE FILES
        $StringSent=urlencode($dir);
        while ($file = readdir($dirHandle)) { 
         // IF IT IS NOT A FOLDER, AND ONLY IF IT IS A .JPG WE ACCESS IT
          if(!is_dir($file) && strpos($file, '.jpg')>0) {
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
         <p>
         Please specify  a file name  (for example, book.json ) to save the selected image location and press "submit"...<br>
         <input type="text"  name="inputdata" size="30">
         </p>
         <br>
         <!--<p>
          Please specify an image filename to save...<br>
          <input type="text" name="outputimgfiletext" size="30">
          </p>

          <p>
          Please specify a json file name for the selected image (example:"filename.json") to save the result...<br>
          <input type="text" name="jsonresultfiletext" size="30">
           </p>-->


         <input style= "font-size: 22px;border: 2px solid #87231C;color: #FF5A51;" type="submit" name="submit" value=Segment>
        
        </form>
         
       </body>
 
       </html>
           
