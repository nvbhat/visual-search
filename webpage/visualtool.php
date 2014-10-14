<html>
<body>

<form align ="left" method="post" action="testdir/asdview_datasaver.html">
<?php
/*echo '<script type="text/javascript" language="javascript">
window.open("testdir/asdview_datasaver.html");
</script>';*/
//session_start();
//echo $_SESSION['variable_name'];
 

$segbookdir="visual-search/books/Segmented-books/";
foreach ($_POST['listallbooks'] as $names)
{
     // echo  $segbookdir.$names;
      echo "Selected book is:".$names;
}


?>
  <br><br>
 <input type="submit" style= "font-size: 28px; color: red;" name="submit" value="Show" >

</form>
</body>
</html>
