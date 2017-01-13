<?php


session_start();

$image=$_SESSION['image'];
$coord=$_SESSION['coord'];
$rating = $_POST['rating'];
$usrname = $_POST['uname'];
$description = $_POST['description'];
$comments = $_POST['comments'];


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
            $selcol = $db->annotation;
            $qry = array("image" => $image,"coord" => $coord);
            $result = $selcol->findOne($qry);
           
           /*if($result)
            {
              echo "update the collection in existing DB";
                          
            }
                else
              {*/

               echo "(NO update) data has to be inserted in the existing DB";
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
               
               //}
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
              $selcol = $db->annotation;
              $qry = array("image" => $image,"coord" => $coord);
              $result = $selcol->findOne($qry);

             /* if($result)
            {
              echo "update the collection in new database";
              
               
            }
             else
            {*/
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
               
              //}
               break;
              }

              
           
     }






?>
