<?php

session_start();

$image=$_SESSION['image'];
$coord=$_SESSION['coord'];
$rating = $_POST['rating'];
$usrname = $_POST['uname'];
$description = $_POST['description'];
$comments = $_POST['comments'];


//$db_data = array();
#echo exec("python python-scripts/mongodb.py");
#phpinfo();

$connection = new MongoClient();
$dbases = $connection->listDBs();
#print_r($dbases);

$num = 0;
foreach ($dbases['databases'] as $dbs) {
         $num++;
        $dbname = $dbs['name'];
         //echo "<br> $num. $dbname";

          if($dbname=='vizsearch-DB')
           {

            echo "it exists";
            $db = $connection->selectDB('vizsearch-DB');
            $collname = "annotation";
            /*$collection = $db->command(array(
            "create" => $collname  
              ));*/
           // $person = array("name" => "Joe", "age" => 20);
            $selcol = $db->annotation;
            
         $qry = array("image" => $image,"coord" => $coord);
         $result = $selcol->findOne($qry);
         if($result)
            {
              echo "update the collection in existing DB";
                          
            }

          else
              {
               echo "NO";
               $document = array( 
               "image" => $image,
               "coord" => $coord,  
               "ratings" => $rating,
               "username" => $usrname,
               "description" =>$description,
               "comments" =>$comments 
                
               
               );

               $selcol->insert($document);
               echo "Document inserted successfully";
               /*$display_qry = array("image" => $image,"coord" => $coord, "ratings" => $rating,
               "username" => $usrname, "description" => $description,"comments" => $comments );
                $result_qry = $selcol->findOne($display_qry);
                foreach ($result_qry as &$value) {
                     //echo $value."\n";
                     array_push($db_data,$value);
                   }*/
                   
                 /*display all information
     $cursor = $selcol->find();
   // iterate cursor to display data of documents
      foreach ($cursor as $document) {
      echo $document["image"] . "\n";
                  }*/
                
              }//end of inside else loop
               /*foreach($db_data as $info)
                  {
                    echo $info;
                    
                  }*/              
 
              break; 
           } 


           else
           {
              echo "create a new database";
              $db = new MongoDB($connection, 'vizsearch-DB');
              $db = $connection->selectDB('vizsearch-DB');
              
              $collname = "annotation";
              $collection = $db->command(array(
              "create" => $collname  
              ));
                //$selcol = $db->annotation;
             //$selcol->insert(array("firstname" => "mkd", "lastname" => "Jones" ));
              //echo "Done";
              $selcol = $db->annotation;
              $qry = array("image" => $image,"coord" => $coord);
              $result = $selcol->findOne($qry);

         if($result)
            {
              echo "update the collection in new database";
              
               
            }

          else
            {
               echo "NO";

               $document = array( 
               "image" => $image,
               "coord" => $coord,  
               "ratings" => $rating,
               "username" => $usrname,
               "description" =>$description,
               "comments" =>$comments 
                
                           
               );

               $selcol->insert($document);
               echo "Document inserted successfully";
               
              }

              break;
           }
     }






?>
