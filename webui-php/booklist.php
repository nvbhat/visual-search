<html>
<head>
<title>
Visual Tool
</title>
</head>
<body>
<p><div style="text-align:left;color:blue;font-size:25px;">Select books from the lists</div></p>
  <form align ="center" method="post" action="testdir/asdview_datasaver.php">
  <select  style="width: 400px;" size="18" name="listallbooks[]" multiple>
       <?php
          
          $allbooks = array();
          $bookdir = "visual-search/books/Segmented-books/";
          $dirControlforbook = opendir($bookdir);
          $StringSentbook=urlencode($bookdir);
          
         while ($bookfile = readdir($dirControlforbook)) {
          if(!is_dir($bookfile) && strpos($bookfile, '.json')>0) {
            
            $allbooks[]=$bookfile;
          }
          
           }
           
           $bookarray_length = count($allbooks);

            for ($i=0;$i<$bookarray_length;$i++)
            {
        ?>
          <option value="<?=$allbooks[$i];?>"><?=$allbooks[$i];?></option>
           <?php
            
            }

           closedir($dirControlforbook);
           ?>

     </select><br>
     
     <input type="submit" style= "font-size: 28px; color: red;" name="submit" value="OK" >
     </form>
</body>
</html>
