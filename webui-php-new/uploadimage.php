<?php
$j = 0;     // Variable for indexing uploaded image.
$target_path = "visual-search/user-uploads";     // Declaring Path for uploaded images.

for ($i = 0; $i < count($_FILES['uploaded_file']['name']); $i++) {

$filename = basename($_FILES['uploaded_file']['name'][$i])
echo $filename;
}
?>
