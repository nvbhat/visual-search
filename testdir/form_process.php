
<head><title>php</title></head>
<body>
Thank you for your contribution.. 
You may leave this page
<?php

$retArr = array();
$retArr["name"] = $_POST['name'];
$retArr["email"] = $_POST['email'];
$retArr["text"]=$_POST['msg'];
//echo json_encode($retArr);
$data=file_get_contents("results.json");
$json=json_decode($data,true);
//$getit=$json
//$json=str_replace(" geometry" ,"644, hello",$json);
$json[]=$retArr;
file_put_contents("results.json", json_encode($json, JSON_PRETTY_PRINT));

?>
</body>
</html>
