<meta content="text/html;charset=utf-8" http-equiv="Content-Type"></meta>
<meta content="utf-8" http-equiv="encoding"></meta>
<link rel="stylesheet" href="css/bootstrap.css"  type="text/css"/>
<link rel="stylesheet" href="css/style.css"  type="text/css"/>
<link rel="stylesheet" href="css/bootstrap-select.css"  type="text/css"/>
<script src="js/jquery.js"></script>
<script src="js/jquery.json-2.4.min.js"></script>
  <script src="js/bootstrap.js"></script>
   <script src="js/bootstrap-select.js"></script>
<script src="js/jquery.validate.min.js"></script>
 <script type="text/javascript">
        $(window).on('load', function () {

            $('.selectpicker').selectpicker({
                'selectedText': 'cat'
            });
            // $('.selectpicker').selectpicker('hide');
        });

</script>
<?php 
//include('mongo.php');
$coord= $_GET['coords'];
$image= $_GET['image'];

?>

<!--<div>
<img src =<?php echo $image ?>  height="500" width="500">
</div>-->

<script type="text/javascript">
 /*var str = window.location.search;
 
    var res = str.split("=");
var symboled = res[1].split("&");
var coord = symboled[0];
image=res[2];
*/
</script>
<body>

<div class="well well-sm" style="text-align:center">
<h3> Share your knowledge</h3>
</div>
<div class="container col-md-8">
      <!--<form action="{{url_for('save_page', image=image,coords=coords)}}" method="POST" class="myfirstform aux | grep apache2 | less role="form">-->
	  <form action="mongo.php" method = "POST">
                   
		<legend>Contact Form</legend>		

            <div class="form-group ">
                <label class="control-label">Rating</label>
                        <div class="controls">
                 <div class="input-group">
<span class="input-group-addon"><i class="glyphicon glyphicon-list"></i></span>
                        <select name="rating" class="form-control selectpicker  show-tick" > <option>1</option>
                                        <option>2</option>
                                        <option>3</option>
                                        <option>4</option>
                                        <option>5</option>
                                        </select>
                                        
                                </div>
                                </div>
                </div>

		<div class="form-group">
	        <label class="control-label">Author</label>
			<div class="controls">
			    <div class="input-group">
<span class="input-group-addon"><i class="glyphicon glyphicon-user"></i></span>	
	<input type="text" class="form-control" name="uname" placeholder="Your Name:">
				</div>
			</div>
		</div>
		
		   <div class="form-group">
                <label class="control-label">Annotation</label>
                        <div class="controls">
                            <div class="input-group">
                                <span class="input-group-addon"><i class="glyphicon glyphicon-envelope"></i></span>
                                        <input type="text" class="form-control" id="text" name="description" placeholder="annotation">
                                </div>
                        </div>  
                </div>

		<div class="form-group">
	        <label class="control-label">Comment</label>
			<div class="controls">
			    <div class="input-group">
				<span class="input-group-addon"><i class="glyphicon glyphicon-envelope"></i></span>
					<input type="text" class="form-control" id="com" name="comments" placeholder="Any comments?">
				</div>
			</div>	
		</div>
		
<!--<div class="form-group ">
                <label class="control-label">Any comments??</label>
                        <div class="controls">
                            <div class="input-group">
                        <span class="input-group-addon"><i class="glyphicon glyphicon-pencil"></i></span>
                                        <textarea name="msg2" class="form-control " rows="4" cols="78" placeholder="write your comment"></textarea>

                                </div>
                        </div>
                </div>
-->		
                           <?php session_start();
                    $_SESSION['image'] =$image;
                    $_SESSION['coord'] = $coord;
                    
                     ?>

	      <div class="controls" style="margin-left: 40%;">
		   <input type="submit" name="submit" value="Save"/>

<!--	       <button type="submit" id="mybtn"  class="btn btn-primary" >Submit</button>-->
	        
	      </div>
		</form>
		</div>
<br />
<br />
<br />

    <hr>

</body>
