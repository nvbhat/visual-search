<html>
<body>

<?php $inputtext = $_POST["inputdata"]; ?>
 

<?php
   $imgdir="visual-search/images/";

   //print "Image Directory path: $imgdir<br/>";
   ?>
      <?php
       
       //$str_data = file_get_contents("visual-search/images/books/data.json");
       //$string = file_get_contents("visual-search/books/book.json");
       //$jsonRS = json_decode ($string,true);
       //foreach ($jsonRS as $rs) {
        //echo stripslashes($rs["book"]["imagedirpath"])." ";
       //echo stripslashes($rs["book"]["imagedirpath"])[0]." ";
            // echo stripslashes($rs["book"]["imagedirpath"])." ";
              // echo stripslashes($rs["country"])." ";
                // echo stripslashes($rs["sports"])."<br>";
      // }
        
         $str_data = file_get_contents("book.json");//read the .json format from book.json file
         $data = json_decode($str_data,true);
        
         foreach ($_POST['dynamic_data'] as $names)
         {
         print "Selected image:$names<br/>";
         $data["book"]["imagedirpath"] = $imgdir.$names;
         //file_put_contents('visual-search/books/'.$inputtext, json_encode($data, JSON_PRETTY_PRINT));
         }

        file_put_contents('visual-search/books/'.$inputtext, json_encode($data, JSON_PRETTY_PRINT));

          //$fh = fopen("visual-search/books/data_out.json", 'w');
                //or die("Error opening output file");
             // fwrite($fh, json_encode($data,JSON_UNESCAPED_UNICODE));
               // fclose($fh);
            
      ?>
   
</body>
</html>
