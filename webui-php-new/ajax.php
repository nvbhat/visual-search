
<?php

$allbooks = array();
 $array = array();
 $bookdir = "visual-search/indexedbooks";
 $dirControlforbook = opendir($bookdir);
   
         while ($bookfile = readdir($dirControlforbook)) {
          if(!is_dir($bookfile) && strpos($bookfile, '.json')>0) {
            
            $allbooks[]=$bookfile;
           
          }
          
           }

 $bookarray_length = count($allbooks);
 for ($i=0;$i<$bookarray_length;$i++)
            {
            // echo json_encode($allbooks[$i]);
             echo $allbooks[$i]."|";
              
               //$array[] = $allbooks[$i];
                //echo $array[i];
         }
     
closedir($dirControlforbook);
 
 


?>
