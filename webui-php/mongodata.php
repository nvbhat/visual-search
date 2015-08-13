<?php
$image = $_POST["image"];
$coord = $_POST["coord"];

$connection = new MongoClient();
$db = $connection->selectDB('vizsearch-DB');
$collection = $db->annotation;
$cursor = $collection->find();
$qry = array("image" => $image,"coord" => $coord);


   // iterate cursor to display title of documents
   foreach ($cursor as $document) {
    if($document["image"]==$image && $document["coord"]==$coord)
   {
     if($document["ratings"]==1)
     {
      echo $document["description"]."\t";
      
     }
     
     }

    
   }

/*$qry = array("image" => $image,"coord" => $coord);
$result = $collection->findOne($qry);

   if($result)
    {
   
     echo $result["description"];
    
    }
    else
     {
      echo "no description available";
      
     }*/

  
?>
