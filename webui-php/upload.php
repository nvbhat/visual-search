<?php
//ini_set('post_max_size', '64M');
//ini_set('upload_max_filesize', '64M');

 // echo $_POST['book'];
 include('config.php');
 $root_dir=$_SERVER['DOCUMENT_ROOT'].$data;
 $target_path = $root_dir."/example-images/user_uploads/";  // Declaring Path for uploaded images.
if (isset($_POST['submit'])) {
 $bookname = $_POST["foldername"];//this is the name of new book user inputs
$selectedimgfiles="";
$returnArray = array();
if (count($_FILES['file']['name']) > 0) {
foreach ($_FILES['file']['name'] as $rs) {

$selectedimgfiles .=$rs."  ";//images as argument("img1.jpg img2.jpg and so on..") format for python script(imagestojson.py)
}
}

//echo $selectedimgfiles;
 $root_dir=$_SERVER['DOCUMENT_ROOT'].$data;
 $target_path = $root_dir."/example-images/user_uploads/";  // Declaring Path for uploaded images.
 //echo $target_path;
 echo exec("python imagestojson.py $selectedimgfiles $bookname $root_dir");//calling the python script for creating a book

$j = 0;     // Variable for indexing uploaded image.

$selectedimages="";   
echo '<center><h4>File upload status :</h4></center>';
for ($i = 0; $i < count($_FILES['file']['name']); $i++) {
// Loop to get individual element from the array
$validextensions = array("jpeg", "jpg", "png", "JPG", "JPEG", "PNG","gif");      // Extensions which are allowed.
$ext = explode('.', basename($_FILES['file']['name'][$i]));   // Explode file name from dot(.)
$file_extension = end($ext); // Store extensions in the variable.
//$target_path = $target_path . md5(uniqid()) . "." . $ext[count($ext) - 1];     // Set the target path with a new name of image.
//$target_path = "example-images/user_uploads/";
$target_path1  = $target_path . $_FILES['file']['name'][$i];
//echo "size:".$_FILES["file"]["size"][$i];
echo '<br >';
$j = $j + 1;      // Increment the number of uploaded images according to the files in array.
if ((($_FILES['file']['error'][$i] === UPLOAD_ERR_OK)&&($_FILES["file"]["size"][$i] < 1000000000 ))    
&& in_array($file_extension, $validextensions)) {
//echo "size:".$_FILES["file"]["size"][$i];
if (move_uploaded_file($_FILES['file']['tmp_name'][$i], $target_path1)) {
// If file moved to uploads folder. 
 echo $j. ').<span id="noerror">Image uploaded successfully!.</span><br/><br/>';
  header("Refresh:4; url=index.php");
//echo $j. ') <img src = "'.$target_path.'" /> <span id="noerror">Image uploaded successfully!.</span><br/><br/>';

} else {     //  If File Was Not Moved.
echo $j. ').<span id="error">please try again!.</span><br/><br/>';
//echo $j. ') <img src = "'.$target_path.'" /> <span id="error">please try again!.</span><br/><br/>';
}
} else {     //   If File Size And File Type Was Incorrect.
   
echo $j. ').<span id="error">***Invalid file Size or Type***</span><br/><br/>';
//echo $j. ') <img src = "'.$target_path.'" /> <span id="error">***Invalid file Size or Type***</span><br/><br/>';
}
}
}
?>
