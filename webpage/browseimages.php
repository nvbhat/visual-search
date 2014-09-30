<html>
 <head>
   <title>Listing Images</title>
    </head>
     <body>
    <p><div style="text-align:center;color:blue;font-size:20px;">select images from the lists and press the "submit" button</div></p>
  <form align ="center" method="post" action="select_imgitems.php">
    <select  style="width: 400px;" size="18" name="dynamic_data[]" multiple>
    <!--<select name="images[]" multiple>-->
      <?php // SPECIFY THE DIRECTORY    
                                                                                           
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
         Please specify the output file name (for example, book.json)<br>
         <input type="text"  name="inputdata" size="30">
         </p>
         <?php
           
         ?>
         <input style= "font-size: 22px;border: 2px solid #87231C;color: #FF5A51;" type="submit" name="submit" value=submit>
        
        </form>
         
       </body>
       </html>
               
