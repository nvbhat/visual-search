<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
	<meta name="viewport" content="width = 1050, user-scalable = no" />

	<link type="text/css" rel="stylesheet" href="css/layout-default-latest.css" />
	<link type="text/css" rel="stylesheet" href="css/tiksluscarousel.css">
	<link type="text/css" rel="stylesheet" href="}css/animate.css" />
	<link type="text/css" rel="stylesheet" href="css/normalize.css" />
	<link type="text/css" rel="stylesheet" href="css/zirsaka.css" />
	<link type="text/css" rel="stylesheet" href="css/ajJAvali.css" />
	<link type="text/css" rel="stylesheet" href="css/NewFile.css" />
        <link rel="stylesheet" href="thumbnailStyle.css">

	<style type="text/css">
	/**
	 *	ALL CSS below is only for cosmetic and demo purposes
	 *	Nothing here affects the appearance of the layout
	 */

	body {
		font-family: Arial, sans-serif;
		font-size: 0.85em;
	}
	

        li {
      list-style: none;
      color: green;
      font-size: 20px;
  
    }
    
      /*.image {
  font-size: 0;
  text-align: center;
  width: 600px;
  height: 500px;
}
img {
  display: inline-block;
  vertical-align: middle;
  max-height: 100%;
  max-width: 100%;
}
.trick {
  display: inline-block;
  vertical-align: middle;
  height: 250px;
}*/
    

   .radiobuttons{
    
    float:right;
    width:300px;
    height:200px;
    border:5px solid cyan;
    display: none;
     padding:8px;
    }


   #frame {
    width:600px;
    padding:8px;
    border:1px solid black;
     display: none;
    }
   
    
   #current_image_container img {
    width:600px;
   }
    #thumbnails_container {
    height:75px;
    border:1px solid black;
    padding:4px;
    overflow-x:scroll;
   
}
.thumbnail {
    border:1px solid black;
    margin-right:4px;
    width:100px; height:75px;
    float:left;
}
.thumbnail img {
    width:100px; height:75px;
}
   
   </style>
	<script type="text/javascript" src="js/jquery-latest.js"></script>
	<script type="text/javascript" src="js/jquery.layout-latest.js"></script>
	<script type="text/javascript" src="js/tiksluscarousel.js"></script>
	<script type="text/javascript" src="js/jquery.zoom.js"></script>
	<script type="text/javascript" src="js/homepage.js"></script>
</head>
<body>

<!-- allowOverflow auto-attached by option: west__showOverflowOnHover = true -->
<div class="ui-layout-west">
	<div id="ajjavali">
	  <div class="accordion-header">Browse Catalogue</div>
	  <div class="add-new-book">Add New Book</div>
          <!--<input class="add-new-book" type="file"  name="file[]" multiple=""  style="font-style:italic">-->
	  <div class="scrollWrap">
	  <div id="bookList" data-id="browse" class="tab-content browse is-active">
		<ol id ="booktest">
                  <!--<li id="book1"><a>Book 1</a></li>
		  <li id="book2"><a>Book 2</a></li>
		  <li id="book3"><a>Book 3</a></li>
		  <li id="booktest"><a>Kandanu.json</a></li> -->
                   <li id="test"></li>                
	        </ol>
	  </div>  
	  </div>
	</div>
</div>

<div class="ui-layout-center">
	<div id="zirsaka">
		<!--<div class="hamburger icon-sidebar" title="Press 'm' to show or hide the menu">Menu</div>-->
		<div title="Press 'm' to show or hide the menu" class="hamburger">
			<svg xml:space="preserve" style="enable-background:new 0 0 96 77;"
				viewBox="0 0 96 77" height="77px" width="96px" y="0px" x="0px"
				xmlns:xlink="http://www.w3.org/1999/xlink"
				xmlns="http://www.w3.org/2000/svg" id="Layer_1" version="1.0">
			<path
				d="M90.000,77.000 C90.000,77.000 6.000,77.000 6.000,77.000 C2.686,77.000 0.000,74.314 0.000,71.000 C0.000,71.000 0.000,6.000 0.000,6.000 C0.000,2.686 2.686,-0.000 6.000,-0.000 C6.000,-0.000 90.000,-0.000 90.000,-0.000 C93.314,-0.000 96.000,2.686 96.000,6.000 C96.000,6.000 96.000,71.000 96.000,71.000 C96.000,74.314 93.314,77.000 90.000,77.000 ZM32.000,4.000 C32.000,4.000 7.000,4.000 7.000,4.000 C5.343,4.000 4.000,5.343 4.000,7.000 C4.000,7.000 4.000,70.000 4.000,70.000 C4.000,71.657 5.343,73.000 7.000,73.000 C7.000,73.000 32.000,73.000 32.000,73.000 C32.000,73.000 32.000,4.000 32.000,4.000 ZM92.000,7.000 C92.000,5.343 90.657,4.000 89.000,4.000 C89.000,4.000 36.000,4.000 36.000,4.000 C36.000,4.000 36.000,73.000 36.000,73.000 C36.000,73.000 89.000,73.000 89.000,73.000 C90.657,73.000 92.000,71.657 92.000,70.000 C92.000,70.000 92.000,7.000 92.000,7.000 ZM24.000,19.000 C24.000,19.000 11.000,19.000 11.000,19.000 C11.000,19.000 11.000,13.000 11.000,13.000 C11.000,13.000 24.000,13.000 24.000,13.000 C24.000,13.000 24.000,19.000 24.000,19.000 ZM24.000,32.000 C24.000,32.000 11.000,32.000 11.000,32.000 C11.000,32.000 11.000,26.000 11.000,26.000 C11.000,26.000 24.000,26.000 24.000,26.000 C24.000,26.000 24.000,32.000 24.000,32.000 ZM24.000,45.000 C24.000,45.000 11.000,45.000 11.000,45.000 C11.000,45.000 11.000,39.000 11.000,39.000 C11.000,39.000 24.000,39.000 24.000,39.000 C24.000,39.000 24.000,45.000 24.000,45.000 Z"
				fill-rule="evenodd" /> </svg>
			Browse
		</div>
		<p>
			<a title="Visual Search" href="/" sl-processed="1"> <img alt="" src="Indic_Visual_Search.jpg" style="max-height:30px;">
		        </a>
		</p>
		<div class="search">
			<form class="search-wrap" action="/search">
				<svg xml:space="preserve" enable-background="new 0 0 50 50"
					viewBox="0 0 50 50" height="50px" width="50px" y="0px" x="0px"
					xmlns:xlink="http://www.w3.org/1999/xlink"
					xmlns="http://www.w3.org/2000/svg" id="Layer_1" version="1.1">
				<circle r="16" cy="20" cx="21" stroke-miterlimit="10"
					stroke-linecap="round" stroke-width="2" fill="none" /> <line
					y2="45.5" x2="45.5" y1="32.229" x1="32.229" stroke-miterlimit="10"
					stroke-width="4" fill="none" /> </svg>
				<input type="text" placeholder="Search" autocomplete="off"
					name="what">
			</form>
		</div>
	</div>
   <!--<div class="image">
  <div class="trick"></div>
  <img id ="myimg"/>
</div>-->

     <div id="frame">
       <div id="current_image_container">
        <img  id="myimg"/>
     </div>
        
       <div id="thumbnails_container">
        <div id="thumbnails_scrollcontainer" style="width : 848px;">
        <!--<div class="thumbnail"><img id="thumbimg" alt="foo" /></div>-->
         
        </div>
      </div> 
</div>
        
      <div class="radiobuttons">

      <p><input type="radio" id="Segment" name="choice" value="Segment">Word Segmenter </p>
      <p><input type="radio" id="Search" name="choice" value="Search">Word Search </p>
      <h3>Select Filter</h3>
      <select class="mobileSelect">
           <option>Remove Wooden Background</option>
           <option>Remove Lines and Points</option>
           <option>Remove hole </option>
                                            
      </select>
      </div>
    <!--<div id="desc">
	<p>Description</p>
    </div>--> 
</div><!--end of center Container-->




<script type="text/javascript">

$(MstrMngr.registerMstrListEvents);

var myLayout;

$(document).ready(function () {

	myLayout = $('body').layout({
		// enable showOverflow on west-pane so popups will overlap north pane
		west__showOverflowOnHover: true
		, class: "ui-layout-center",
                
	});
        
  
});

</script>
<script  type="text/javascript">


  $(document).ready(function(){

   $.ajax({
  url:"ajax.php",
  type:"GET",

  success:function(msg){
  id_numbers = msg;
  var data=[];
  var splitdata=msg.split("|");
 for(i=0;i<splitdata.length-1;i++)
{
  data.push(splitdata[i]);

}
 for(var i=0;i<data.length;i++){
          $("ol").append("<li><a>"+data[i]+"</a></li>"); 
        }//end of for-loop

        $("#booktest li").click(function(){
              //alert($(this).text());
              var book = $(this).text();
               alert(book);

               var request = $.ajax({
  url: "readimages-from-json.php",
  type: "POST",
  data: {book:book},
  dataType: "html"
});

request.done(function(allimages) {
  //alert(allimages);
var splitimg= allimages.split("|");

var iDiv = new Array();
var iImg =new Array();

//function for displaying each clicked thumbnail image in main image viewer
function display($this) {
    var source = $("img", $this).attr("src");
    //alert("The souce of the image is " + source);

   
   document.getElementById("myimg").src=source;
   
}
//display of the first image in main image view window
document.getElementById("myimg").src=splitimg[0];
for(var i=0;i<splitimg.length-1;i++)
{
  
   //Dynamically put images in thumbnail viewer

   //Code for creating dynamic div for thumbnail views
   iDiv[i] = document.createElement('div');
   iDiv[i].id = i;
   iDiv[i].className = 'thumbnail';
   document.getElementById('thumbnails_scrollcontainer').appendChild(iDiv[i]);
   
   //Code for displaying images in the thumbnail div dynamically
   //var img = $('<img id="dynamic">'); //Equivalent: $(document.createElement('img'))
    iImg[i]=$(document.createElement('img'));
    iImg[i].id=  iDiv[i].id ;
    iImg[i].attr('src', splitimg[i]);
    iImg[i].appendTo(iDiv[i]);
   
    //var imgObject1 = document.getElementById(iDiv[i].id);
     //var src =imgObject1.getElementsByTagName('img')[0].src;
     

    $('#' +iDiv[i].id).click(function() {
     //alert("hello");

     display($(this));
   
   //document.getElementById("myimg").src="test.jpg";
   });
   
   
}


//document.getElementById("thumbimg").src="test.jpg";
  $("#frame").toggle(); 
  $(".radiobuttons").toggle();
});

request.fail(function(jqXHR, textStatus) {
  alert( "Request failed: " + textStatus );
});

            });//end of click function

}//end of sucess function
});//end of main-ajax

   
       
});






function go()
{
  alert("starting");
}
 function processBook()
{
   //alert(book);
}
 function processImg(img){
   //document.getElementById("myimg").src=img;
}
	
</script>


</body>
</html>
