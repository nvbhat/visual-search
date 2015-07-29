<?php
//echo $_POST['imgname'];
$imagefile= $_GET['image_to_search'];
//echo $_GET['book'];
$book= $_GET['bookname'];

//echo $imagefile;
?><!DOCTYPE html>
<html lang="en">
<head>
  <title>visual search</title>
  <meta http-equiv="Content-type" content="text/html;charset=UTF-8" />
  <script src="../js/jquery.min.js"></script>
  <script src="../js/jquery.Jcrop.js"></script>
  <link rel="stylesheet" href="demo_files/main.css" type="text/css" />
  <link rel="stylesheet" href="demo_files/demos.css" type="text/css" />
  <link rel="stylesheet" href="../css/jquery.Jcrop.css" type="text/css" />

<script type="text/javascript">

  $(function(){

    $('#cropbox').Jcrop({
       //aspectRatio: 1,
      onSelect: updateCoords
    });

  });

  function updateCoords(c)
  {
    $('#x').val(c.x);
    $('#y').val(c.y);
    $('#w').val(c.w);
    $('#h').val(c.h);
  };

  function checkCoords()
  {
    if (parseInt($('#w').val())) return true;
    alert('Please select a crop region then press submit.');
    return false;
  };

</script>
<style type="text/css">
  #target {
    background-color: #ccc;
    width: 500px;
    height: 330px;
    font-size: 24px;
    display: block;
  }


</style>

</head>
<body>

<div class="container">
<div class="row">
<div class="span12">
<div class="jc-demo-box">

<div class="page-header">
<h1>Select any area of the image and press search</h1>
</div>

	               <img src= <?php echo $imagefile ?>  id="cropbox" />
       	                <form action="process_search.php" method="POST" >

                        <?php
                      session_start();
                    $_SESSION['srcimage'] =$imagefile;
                    $_SESSION['bookname'] = $book;
                          ?>
         		<input type="hidden" id="x" name="x" />
			<input type="hidden" id="y" name="y" />
			<input type="hidden" id="w" name="w" />
			<input type="hidden" id="h" name="h" />

                        Set Threshold <input type="text" name="threshold" value=""><br>
			<input type="submit" value="search" class="btn btn-large btn-inverse" />
		</form>


	</div>
	</div>
	</div>
	</div>
	</body>

</html>
