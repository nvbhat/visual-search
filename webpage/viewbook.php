<html>
<title>
Image Segmentation
</title>

<body>
<!--<h1><div style="text-align:center;color:red;font-size:35px;">view segmented books</div></h1>-->

   <?php $inputtext = $_POST["inputdata"]; ?>
 

   <?php
   $imgdir="visual-search/images/";
   ?>

      <?php
       
         $str_data = file_get_contents("book.json");//read the .json format from book.json file
         $data = json_decode($str_data,true);
        
         foreach ($_POST['dynamic_data'] as $names)
         {
         //print "Selected image:$names<br/>";
         $data["book"]["imagedirpath"] = $imgdir.$names;
         }

        file_put_contents('visual-search/books/'.$inputtext, json_encode($data, JSON_PRETTY_PRINT));
       // echo $data["book"]["imagedirpath"];

        $inputimg=$data["book"]["imagedirpath"];
        //echo $inputimg;
        //code for inputting three parameters("book.json,rect-result.jpg,rectsegment.json)
        //$segmentedimg=$_POST["outputimgfiletext"];
        //$jsonresultfile=$_POST["jsonresultfiletext"];

        //$resultimgpath="visual-search/images/segmented-images/","$segmentedimg";
       // echo "visual-search/images/segmented-images/","$segmentedimg";
        
       
       

   //code for inputting three parameters to the ImageSegmenter c++ file without spliting string)
   //exec("./ImageSegmenter $inputimg visual-search/images/segmented-images/$segmentedimg visual-search/books/Segmented-books/$jsonresultfile");
   
   
   $splitstr=split(".jpg",$names);
   $segmentedimg=$splitstr[0]."-result.jpg";
   $jsonresultfile=$splitstr[0]."-result.json";
  
   exec("./ImageSegmenter $inputimg visual-search/images/segmented-images/$segmentedimg visual-search/books/Segmented-books/$jsonresultfile");
      
   //echo '<script type="text/javascript">("Segmented books are successfully saved ")</script>';
        
    // print "Segmented books are successfully saved"         
      
     ?>

   <!-- <p><div style="text-align:left;font-size:24px;">Segmented books are successfully saved</div></p>-->
   
   <form align ="left" method="post" action="visualtool.php">
    <p><div style="text-align:left;color:blue;font-size:20px;">Select segmented books from the list</div></p>
   <!-- <select  style="width: 400px;" size="18" name="listallbooks[]" multiple><br>-->
  <!--<input type="submit" style= "font-size: 22px;color: red;" name="submit1" value="view segmented-books" ><br><br>-->
   <!--<input type="submit" style= "font-size: 22px;color: blue;" name="submit2" value="view unprocessed books" ><br><br>
    <input type="submit" style= "font-size: 22px;color: green;" name="submit3" value="view user-annotated books" >-->
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

   <!-- <form action="imgsegment.php" method="POST">
    <p>
    Please specify an image filename to save...<br>
    <input type="text" name="outputimgfiletext" size="30">
    </p>
    <input type="submit" style= "font-size: 22px;color: green;" name="submit" value="Segment" ></button>
    </form>-->

 
</body>
</html>
