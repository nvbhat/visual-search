<!DOCTYPE html>
<html>
<head>
<title>IISc - Upload images</title>
<style>
@import "http://fonts.googleapis.com/css?family=Droid+Sans";
form{
background-color:#fff
}
#maindiv{
width:960px;
margin:10px auto;
padding:10px;
font-family:'Droid Sans',sans-serif
}
#formdiv{
width:600px;
float:left;
text-align:center
}
form{
padding:40px 20px;
box-shadow:0 0 10px;
border-radius:2px
}
h2{
margin-left:30px
}
.upload{
background-color:#c20b0b;
border:1px solid black;
color:#fff;
border-radius:5px;
padding:10px;
text-shadow:1px 1px 0 green;
box-shadow:2px 2px 15px rgba(0,0,0,.75)
}
.upload:hover{
cursor:pointer;
background:green;
border:1px solid black;
box-shadow:0 0 5px rgba(0,0,0,.75)
}
#file{
color:green;
padding:12px;
border:1px dashed #123456;
background-color:#ebebeb;
}
#upload{
margin-left:45px
}
#noerror{
color:green;
text-align:left
}
#error{
color:red;
text-align:left
}
#img{
width:17px;
border:none;
height:17px;
margin-left:-20px;
margin-bottom:91px
}
.abcd{
text-align:center
}
.abcd img{
height:100px;
width:100px;
padding:5px;
border:1px solid #e8debd
}
b{
color:red
}
#phparea {
	height : 300px;
	background-color : #yellow;
	overflow-y: auto;
	box-shadow:0 0 10px;
	border-radius:2px;
	text-align : left;
	padding-left : 30px;
	margin-top : 10px;
}
#phparea img{
	border : 1px solid black;
	height : 30px;
	width  : 40px;
}

#phparea::-webkit-scrollbar {
    width: 1em;
}
#phparea::-webkit-scrollbar-track {
    -webkit-box-shadow: inset 0 0 6px rgba(0,0,0,0.3);
    background : #ebebeb;
}
#phparea::-webkit-scrollbar-thumb {
  background-color: gray;
  outline: 1px solid #6377DA;
}
</style>


<!-------Including jQuery from Google ------>
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>


 
<!------- Including CSS File ------>

<body>
<div id="maindiv">
<div id="formdiv">
<center>
<h2>Upload a new book</h2>
<form enctype="multipart/form-data" action="" method="post">
Choose files to upload<br ><br >
<div id="filediv"><input name="file[]" type="file" id="file" multiple="" onClick = "clearArea()"/></div><br >
<p style="font-family:Tomaha;font-size:20px;color:black"><b>Name the new book.  <input type="text" name="foldername" method="post"></p>
<input type="submit" value="Upload file(s)" name="submit" id="upload" class="upload"/>
</form>
</center>
<!------- Including PHP Script here ------>
<div id = "phparea"><?php include "upload.php"; ?></div>
</div>
</div>
<script>
var disp = 0;
function clearArea(){
	$("#phparea").empty();
}


</script>
</body>
</html>
