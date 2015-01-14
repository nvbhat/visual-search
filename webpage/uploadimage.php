<?php
   
//Сheck that we have a file
if((!empty($_FILES["uploaded_file"])) && ($_FILES['uploaded_file']['error'] == 0)) {
  //Check if the file is JPEG image and it's size is less than 1.4MB
  $filename = basename($_FILES['uploaded_file']['name']);
  $ext = substr($filename, strrpos($filename, '.') + 1);
 
 // if ((($ext == "jpg")||($ext=="png")) && (($_FILES["uploaded_file"]["type"] == "image/jpeg")||($_FILES["uploaded_file"]["type"] == "image/png")) &&
   if (($ext == "jpg") && ($_FILES["uploaded_file"]["type"] == "image/jpeg") && ($_FILES["uploaded_file"]["size"] < 10485760))
    {
    
    //Determine the path to which we want to save this file
      $newname = dirname(__FILE__).'/visual-search/images/user-upload/'.$filename;
      //Check if the file with the same name is already exists on the server
    
      
      if (!file_exists($newname)) {
        //Attempt to move the uploaded file to it's new place
        if ((move_uploaded_file($_FILES['uploaded_file']['tmp_name'],$newname))) {
           
           echo "Upload Complete! ";
          //print "User Upload Completed ";
        } else {
           echo "Error: A problem occurred during file upload!";
        }
      } else {
         echo "Error: File ".$_FILES["uploaded_file"]["name"]." already exists";
      }
  } else {
     echo "Error: File too big to upload";
  }
} else {
 echo "Error: No file uploaded";
}


?>
