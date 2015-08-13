<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
 <head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8" />
        <title>Visual-Search Tool</title>
	<meta name="description" content="Visual-Search Tool" />
	<link href="default.css" rel="stylesheet" type="text/css" media="screen" />
	<link rel="stylesheet" href="css/example.css" />
	<link rel="stylesheet" href="css/easyzoom.css" />
        
        <script type="text/javascript" src="js/d3.v2.js"></script>
         <script type="text/javascript" src="js/d3.v3.min.js"></script>
        <script type="text/javascript" src="js/d3.tip.v0.6.3.js"></script>

       <script src="crop/js/jquery.min.js"></script>
       <script src="crop/js/jquery.Jcrop.js"></script>
       <!--<link rel="stylesheet" href="crop/demos/demo_files/main.css" type="text/css" />-->
       <link rel="stylesheet" href="crop/demos/demo_files/demos.css" type="text/css" />
       <link rel="stylesheet" href="crop/css/jquery.Jcrop.css" type="text/css" />
       <link rel="stylesheet" href="crop/css/button_view.css" type="text/css" />


<style>
table {
  border-spacing: 15px 0;
}


/*d3.js css code*/

.d3-tip {
  line-height: 1;
  font-weight: bold;
  padding: 12px;
  background: rgba(0, 0, 0, 0.8);
  color: #fff;
  border-radius: 2px;
}

/* Creates a small triangle extender for the tooltip */

.d3-tip:after {
  box-sizing: border-box;
  display: inline;
  font-size: 10px;
  width: 100%;
  line-height: 1;
  color: rgba(0, 0, 0, 0.8);
  content: "\25BC";
  position: absolute;
  text-align: center;
}


#tag1,#tag2,#tag3,#tag4{
background-color : white;
text-decoration : none;
padding : 5px;
border : 1px solid black;
border-radius : 8px;
margin : 5px;
}

#tag2{
padding-right : 65px;
text-align : center;
}

#tag4{
padding-right : 35px;
text-align : center;
}
#tag4:hover{
//padding : 7px;
//padding-right : 37px;
background : green;
}

#tag2:hover{
//padding : 7px;
//padding-right : 67px;
background : orange;
}
#tag3:hover{
//padding : 7px;
background : yellow;
}
#tag1:hover{
//padding : 7px;
background : cyan;
}

/* Style northward tooltips differently */

.d3-tip.n:after {
  margin: -1px 0 0 0;
  top: 100%;
  left: 0;
}


</style>


<!--code for image croop -------->
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


</head>

<body>  
<?php
session_start();
include('config.php');
//include('mongo.php');
//$mongodata = $_SESSION['varname'];

$root_dir=$_SERVER['DOCUMENT_ROOT'].$data;
?>
<script>

  var relpath_dir ="<?php echo $data; ?>";
  var img_dir=relpath_dir+"/example-images/user_uploads/";
</script>
 
<div id="entire">
	<div id="matter_bg">
		<div id="heading">
			Visual-Search and Word Segmenter Tool
		</div>
		<div class="clear"></div>
	<div id = "content">
	
		<div id = "navl">
		<!--	<div class="upload">
				<input type="file" id="files" name="files[]" multiple style = "width: 130px; height: 40px; padding-left:25px; padding-top:10px; z-index : 2; opacity :0;"/>
			</div>
		-->
                 <a href="multiupload.php"><div class="upload"></div></a><br /><br />
		<h2>Book Lists</h2>
		
		<div class = "jsonlistarea">
			<!--<ul>
			<a href = "#"><li>Json 1</li></a>
			<a href = "#"><li>Json 2</li></a>
			<a href = "#"><li>Json 3</li></a>
			</ul>
			-->
			<?php
                
		$folder = $root_dir.'/books/';		
	$filetype = '*.'.'json';
	$files = glob($folder.$filetype);
	if($files){ 
	echo '<ul onclick="getjsonname(event);">';
	$count = count($files);
	for ($i = 0; $i < $count; $i++) {
	echo '<a  href="#"><li>'.substr($files[$i],strlen($folder),strpos($files[$i], '.')-strlen($folder)).'.json</li></a>';
	}
	echo '</ul>';
	}	
	else
	echo '<br ><center><h3>"No JSON files found in the directory"</h3></center>';	
		?>
		</div>
		<br ><br> <h4 id = "whichjson"> </h4> 
		</div>

		
		
	<!--	<form enctype="multipart/form-data" action="crop/demos/search.php" method="POST" >-->
	<div id = "image_area">
		<div id="example">
			<div class="easyzoom easyzoom--overlay easyzoom--with-thumbnails">
				<a href = "#" id="atag">
					<img src="images/first.png" id="mainimg"  alt="" width="542" height="346" />
				</a>
			</div>
                         <center><span id = "demo"  name="imgname"> Current Image:</span></center> 
			<div class = "thumbimg">
     
			<ul class="thumbnails">
                        <!--<div id = "image123">
                        </div>-->

		      </ul>	
			
			</div>
		</div>
	</div>


		
		<div id = "navr">
		<h2>Results</h2>
		<br />

       <div id ="aaa">
         </div>
           <div id="radio_area">
           <table>
            <tr><td>
                <h3 style=" color: red;">Select Segmentation Types</h3>
		<!--<input id ="segment" type="radio" name="scannedimage" value="op1" onClick="segment_scannedimages(this.value)">Segment Scanned type Images<br />
<input type="radio" name="otherimage" value="op2" onClick="segment_otherimages(this.value)">Segment Other Images<br />-->
<a href ="#" id = "tag1" onClick="segment_scannedimages(this.value)">Segment Scanned type Images</a><br />
<a href ="#" id = "tag2" onClick="segment_otherimages(this.value)">Segment Other Images</a><br />

		

                 </td><td>
                  
                <!--<input type="radio" name="tempmatch" value="op3" onClick="template_search(this.value)">Template Match<br />
                <input type="radio" name="flannmatch" value="op4" onClick="flann_search(this.value)">Flann Match<br>-->
                     
                       <h3 style=" color: blue;">Visual Search</h3>
		<!--<input type="radio" id="tempmatch" name="tempmatch" value="op3"  >Template Match<br />
		<input type="radio" id="flannmatch" name="flannmatch" value="op4" >Flann Match<br>-->

 <a href ="#" id = "tag3" target = "_blank" onClick = "visualsearch(this.form)">Template Match</a><br />
 <a href ="#" id = "tag4" target = "_blank" onClick = "visualsearch(this.form)">Flann Match</a><br />
                
               
                        <!--<input type="hidden" id="x" name="x" />
			<input type="hidden" id="y" name="y" />
			<input type="hidden" id="w" name="w" />
			<input type="hidden" id="h" name="h" />-->
                     <!--<input type="submit" value="search" onclick="visualsearch(this.form)" class="btn btn-large btn-inverse" />
                        <input type="submit" value="search" onclick="visualsearch(this.form)"   class="btn btn-large btn-inverse" />
                    </form>--><!--form tag ends here-->
                </td></tr>
                 </table>
                  
                 </div>
		</div>
	</div>		
	</div>
</div>

	

<!--<script src="https://code.jquery.com/jquery-1.10.2.min.js"></script>-->
	<script src="dist/easyzoom.js"></script>
	<script>
$("#navr h2").empty();
document.getElementById('demo').innerHTML = "css/imgs/first.png";
		var source="";
		// Instantiate EasyZoom instances
		var $easyzoom = $('.easyzoom').easyZoom();

		// Get an instance API
		var api = $easyzoom.filter('.easyzoom--with-thumbnails').data('easyZoom');
                
		// Setup thumbnails example
		$(".thumbnails").on("click", "a", function(e) {
                     $("#navr h2").empty();
			var $this = $(this);
                         
			e.preventDefault();

			// Use EasyZoom's `swap` method
			api.swap($this.data("standard"), $this.attr("href"));
                       
                      source = $this.attr("href");
                      document.getElementById("mainimg").src=source;
                       //document.getElementById("mainimg").src="s3.jpg";
                        $("#aaa").empty();           
                   $('input[name=scannedimage]').attr('checked',false);
                   $('input[name=otherimage]').attr('checked',false);
                   $('input[name=tempmatch]').attr('checked',false);
                   $('input[name=flannmatch]').attr('checked',false);
                    
               
		});
		
		function getName(_src){
 document.getElementById('demo').innerHTML = _src;
            // alert(_src);
    
    	}
		
var x = 0;
function getjsonname(event) {
       
       if(x!=0){
$("#navr").toggle(); 
$("#navr").toggle(); 
$("#whichjson").toggle(); 
$("#whichjson").toggle(); 
}else{
$("#navr").toggle(); 
$("#whichjson").toggle(); 
}
 x =x +1;
     
       var target = event.target || event.srcElement;
       document.getElementById('whichjson').innerHTML = event.target.innerHTML;
     var book = event.target.innerHTML;
//var dir="example-images/user_uploads/";
var dir=img_dir;
var iDiv = new Array();
var iImg =new Array();
        
  var request = $.ajax({
  url: "imagelist.php",
  type: "POST",
  data: {book:book},
  dataType: "html"
  });//request method ends       


   request.done(function(imglist) {
      $(".thumbnails").empty();
    var splitimg= imglist.split("|");
  
   for(var i=0;i<splitimg.length-1;i++)
   {

   $(".thumbnails").append("<li><a href = '"+dir+splitimg[i]+"' data-standard = '"+dir+splitimg[i]+"'><img src="+dir+splitimg[i]+" onclick = 'getName(this.src)' width = 140px height = 120px></a><br>"+splitimg[i]+"</li>"); 
   
    
   }
      
     });

    request.fail(function(jqXHR, textStatus) {
  alert( "Request failed: " + textStatus );
});

	 
     
    } 

  function segment_scannedimages(para)
  {
                       // $("#navr h2").toggle(); 
                         $("#navr h2").html("Results")
                       var source1=document.getElementById("mainimg").src;
                        //alert(source1);
                       
                        //source = source1;
                      
                       var dir=img_dir;
                       var fname= source.split("/").slice(0, -1).join("/")+"/";    
                       var splitfname = source.split(fname);
                       var imagefile = splitfname[1];
                       var source1=imagefile;
                       var splitimagefile = imagefile.split(".");
                       var imagename=splitimagefile[0];
                       //alert(imagename); 
                       var imagejsonfilename= imagename+"-result.json"; 
                       source=source1;

                       
                       var request = $.ajax({
                                       url: "ajax1.php",
                                       type: "POST",
                                       data: {imagefile:source,segmentimage:imagejsonfilename},
                                       dataType: "html"
                                        });//ajax request method ends

                              request.done(function(segmentedbook) {
                                        var resultbook=segmentedbook;
          //start d3.js
           alert(resultbook);
                   d3_img_source=img_dir+imagefile;
                   var svg = d3.select("#navr")
                        .select("#aaa")
			//.select(".easyzoom easyzoom--overlay easyzoom--with-thumbnails")
                        
                        // .select("#atag")
                         //.select("#mainimg")
			.append("svg")
			.attr("width","1400")
			.attr("height","1400")
		        .style("border", "1px solid black")
                        .append('svg:g')
		        .call(d3.behavior.zoom().on("zoom", redraw));
	               
            var tip = d3.tip()
		  .attr('class', 'd3-tip')
		  .offset([-10, 0])
		  .html(function(d) {
	    return "<strong>name:</strong> <span style='color:red'>" + d.text + "</span>";});
	    svg.call(tip);
             //alert("sucess");
       
               d3.json(resultbook,
                function(error,test) 
                {
                      //alert("inside");
                     //alert(resultbook);
			//console.log(test.imagepath);
                       //alert(test.imagepath);
                      // alert("Location:"+source);
			var imgs = svg.selectAll("image").data([0])
				.enter()
				.append("svg:image")
				.attr('image-rendering','optimizeQuality')
				.attr("xlink:href", d3_img_source)
				.attr("x", "0")
				.attr("y", "0");
			var img = new Image();
			img.src=d3_img_source;
			img.onload=function(){
					var width=this.width;
					var height=this.height;
					//var width= 365;
					//var height= 365;
                                        //alert("width : "+width);
				    imgs.attr("width", width)
					.attr("height",height);
			}
			//Draw the Rectangle
			 var rectangle = svg.selectAll("rect").data(test.segments)
                                 
				.enter()
				.append("svg:rect")
				.attr("class","overlay")
				.attr("pointer-events", "all")
				.attr("x", function (d) { return d.geometry.x; } )
				.attr("y", function (d) { return d.geometry.y; } )
				.attr("width", function (d) { return d.geometry.height; } )
				.attr("height", function (d) { return d.geometry.width; } )
				.style("fill-opacity",0.2)
				.attr('fill',function (d) { return "blue"; } )
				//.on('mouseover',tip.show)
				//.on('mouseout',tip.hide)
		                .on("click",function goToURL(c) {
                                             //alert("helooo");
					jsondata = [c.geometry.x,c.geometry.y,c.geometry.height,c.geometry.width];
                                        //alert(image);
 					alert(jsondata);
			  		//location.href="/form?coords="+jsondata+"&image="+image;
				    })
                                .on('mouseover', function(d){
                                         alert("hello");
                                        });
                              
		}

	);//end of d3.json method

            function redraw() 
         {
	//console.log("here", d3.event.translate, d3.event.scale);
	svg.attr("transform", "translate(" + d3.event.translate + ")scale(" + d3.event.scale + ")");
         }
    
          
          //end of d3
                                   });//end of request.done method

                              request.fail(function(jqXHR, textStatus) {
                                   alert( "Request failed: " + textStatus );
                                   });
  
               
  }
   
   function segment_otherimages(args)
    {
        $("#navr h2").html("Results")
        //$("#navr h2").toggle(); 
       alert("segment other images");
         var source1=document.getElementById("mainimg").src;
          
                     
                       var dir=img_dir;
                       var fname= source.split("/").slice(0, -1).join("/")+"/";    
                       var splitfname = source.split(fname);
                       var imagefile = splitfname[1];
                       var source1=imagefile;
                       var splitimagefile = imagefile.split(".");
                       var imagename=splitimagefile[0];
                       //alert(imagename); 
                       var imagejsonfilename= imagename+"-result.json"; 
                       source=source1;
             //alert(source1);
                        var request = $.ajax({
                                       url: "ajax2.php",
                                       type: "POST",
                                       data: {imagefile:source,segmentimage:imagejsonfilename},
                                       dataType: "html"
                                        });//ajax request method ends

                              request.done(function(segmentedbook) {
                                        var resultbook=segmentedbook;
                                        // alert(resultbook);


                                      //start d3.js
            alert(resultbook);
                     d3_img_source=img_dir+imagefile;
                     var svg = d3.select("#navr")
                        .select("#aaa")
			//.select(".easyzoom easyzoom--overlay easyzoom--with-thumbnails")
                        
                        // .select("#atag")
                         //.select("#mainimg")
			.append("svg")
			.attr("width","1400")
			.attr("height","1400")
		        .style("border", "1px solid black")
                        .append('svg:g')
		        .call(d3.behavior.zoom().on("zoom", redraw));
	    var data = "";     
            var tip = d3.tip()
		  .attr('class', 'd3-tip')
		  .offset([-10, 0])
		  .html(function(d) {
                   var text = "meaning of the text is ...........";
                   var jsondata= [d.geometry.x,d.geometry.y,d.geometry.height,d.geometry.width];
                   jsondata_string= jsondata.toString(); 
                                       
                                       var request = $.ajax({
                                       url: "mongodata.php",
                                       type: "POST",
                                       data: {image:d3_img_source,coord:jsondata_string},
                                       dataType: "html"
                                        });//ajax request method ends
                                     request.done(function(info) {
                                           data = info;
                                         });
                                       request.fail(function(jqXHR, textStatus) {
                                   alert( "Request failed: " + textStatus );
                                   });
              
                   //var data = "<?php echo $mongodata; ?>";
                  //jsondata = [d.geometry.x,d.geometry.y,d.geometry.height,d.geometry.width];
	     return "<strong>Description:</strong> <span style='color:red'>" + data+ "</span>";});
	    svg.call(tip);
     //alert("sucess");
       
     d3.json(resultbook,
                function(error,test) 
                {
                      //alert("inside");
                     //alert(resultbook);
			//console.log(test.imagepath);
                       //alert(test.imagepath);
                      // alert("Location:"+source);
			var imgs = svg.selectAll("image").data([0])
				.enter()
				.append("svg:image")
				.attr('image-rendering','optimizeQuality')
				.attr("xlink:href", d3_img_source)
				.attr("x", "0")
				.attr("y", "0");
			var img = new Image();
			img.src=d3_img_source;
			img.onload=function(){
					var width=this.width;
					var height=this.height;
					//var width= 365;
					//var height= 365;
                                        //alert("width : "+width);
				    imgs.attr("width", width)
					.attr("height",height);
			}
			//Draw the Rectangle
			 var rectangle = svg.selectAll("rect").data(test.segments)
                                 
				.enter()
				.append("svg:rect")
				.attr("class","overlay")
				.attr("pointer-events", "all")
				.attr("x", function (d) { return d.geometry.x; } )
				.attr("y", function (d) { return d.geometry.y; } )
				.attr("height", function (d) { return d.geometry.height; } )
				.attr("width", function (d) { return d.geometry.width; } )
				.style("fill-opacity",0.2)
				.attr('fill',function (d) { return "blue"; } )
                                
				.on('mouseover',tip.show)
				.on('mouseout',tip.hide)
		                .on("click",function goToURL(c) {
                                        
					jsondata = [c.geometry.x,c.geometry.y,c.geometry.height,c.geometry.width];
                                        //alert(jsondata);
		    	  		location.href="form.php?coords="+jsondata+"&image="+d3_img_source;
                                                              
				    })
                                 /*.on('mouseover', function(c){
                                         //alert("hello");

                                        jsondata = [c.geometry.x,c.geometry.y,c.geometry.height,c.geometry.width];
                                        
                                        });*/
                              
                              
		                }

                 	);//end of d3.json method

            function redraw() 
         {
	//console.log("here", d3.event.translate, d3.event.scale);
	svg.attr("transform", "translate(" + d3.event.translate + ")scale(" + d3.event.scale + ")");
         }
    
          
          //end of d3
                                         
                                        });//end of request.done method

                     request.fail(function(jqXHR, textStatus) {
                                   alert( "Request failed: " + textStatus );
                                   });



                                    
     }



   //************************code for visual search *************************************//
     
        function visualsearch(form)
         {

                 var book= document.getElementById('whichjson').innerHTML;
                 var image=document.getElementById("mainimg").src;
               
               document.getElementById("tag3").href = "crop/demos/search.php?image_to_search=" + image + "&bookname=" + book;
               document.getElementById("tag4").href = "crop/demos/searchui_flann.php?image_to_search=" + image + "&bookname=" + book;
                      
           
         }
     
         
     
		</script>


    <!--<?php
      session_start();
    $srcimage=$_SESSION['srcimage'];
    echo $srcimage;
   ?>-->
</body>
</html>

