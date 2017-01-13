<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="content-type" content="text/html; charset=utf-8" />
<title>Visual-Search Tool</title>
<meta name="description" content="Visual-Search Tool" />
<link rel="stylesheet" href="css/default.css" />
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


</head>

<body>  
<?php
session_start();
include('config.php');

$root_dir=$_SERVER['DOCUMENT_ROOT'].$data;
?>

<script>
var relpath_dir ="<?php echo $data; ?>";
var img_dir=relpath_dir+"/example-images/user_uploads/";
</script>

<div id="webpage">
    <div id="page_background">
        <div id="heading">
            Visual Search for Indic Texts
        </div>
        <div id = "content">
            <div id = "navl">
                <a href="multiupload.php">Upload</a><br /><br />
                <h2>Books Available:</h2>
                <br>
                <div class = "booklist">
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
                            echo '<br ><center><h3>"No books found. Try uploading one."</h3></center>';	
                    ?>
                </div>
                <br><br>
                <h4 id="selbook_name"></h4> 
                <h2>Controls:</h2>
                <div id="controls">
                    <form id="ctl_parms" action="alert('form submitted');">
                    <button id=img_search>Image Search</button>
                    <br/><br/>
                    <table>
                        <tr>
                            <td>
                                Auto-segment:
                                <input type="checkbox" id="autoseg" checked/>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <p title="Used for matching">Image Quality:</p>
                            </td>
                            <td>
                                <select name="img_quality">
                                    <option value=template>Clean Image</option>
                                    <option value=flann>Noisy image</option>
                                </select>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                Doc Type:
                            </td>
                            <td>
                                <select name="img_type">
                                    <option value=printed>Printed Text</option>
                                    <option value=talapatra>Palm leaf</option>
                                    <option value=paper>Paper Manuscript</option>
                                    <option value=scan>Scanned Image</option>
                                    <option value=photo>Photo</option>
                                </select>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                Text Orientation:
                            </td>
                            <td>
                                <select name="img_angle">
                                    <option value=horizontal>Horizontal text</option>
                                    <option value=irregular>Irregular formatting</option>
                                </select>
                            </td>
                        </tr>
                    </table>
                    </form>
                </div>
            </div>

            <div id ="status">Server Response:</div>
            <div id = "book_display">
                <div class = "thumbimg">
                    <ul class="thumbnails"></ul>	
                </div>
                <div class="easyzoom easyzoom--overlay easyzoom--with-thumbnails">
                    <a href = "#" id="atag">
                        <img src="images/first.png" id="selected_img"  alt=""
                        width="1000px"/>
                    </a>
                </div>
                <center><span id = "demo"  name="imgname">Current Image:</span></center> 
            </div>

            <div id = "navr">
<!--
                                <h3 style=" color: red;">Select Segmentation Types</h3>
                                <a href ="#" id = "tag1" onClick="segment_scannedimages(this.value)">Segment Scanned type Images</a><br />
                                <a href ="#" id = "tag2" onClick="segment_otherimages(this.value)">Segment Other Images</a><br />
                            </td>
                            <td>
                            <h3 style=" color: blue;">Visual Search</h3>

                            <a href ="#" id = "tag3" target = "_blank" onClick="visualsearch(this.form)">Template Match</a><br />
                            <a href ="#" id = "tag4" target = "_blank" onClick="visualsearch(this.form)">Flann Match</a><br />

                            </td>
                        </tr>
-->
                <h2>Results</h2>
                <br/>

            </div> <!-- navr -->
        </div> <!-- content -->
    </div> <!-- page_background -->
</div> <!-- webpage -->

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

// When a thumbnail image is clicked, show it as selected image and zoom
$(".thumbnails").on("click", "a", function(e) {
        $("#navr h2").empty();
        var $this = $(this);

        e.preventDefault();

        // Use EasyZoom's `swap` method
        api.swap($this.data("standard"), $this.attr("href"));

        source = $this.attr("href");
        document.getElementById("selected_img").src = source;
        $("#status").empty();           
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
        $("#selbook_name").toggle(); 
        $("#selbook_name").toggle(); 
    }else{
        $("#navr").toggle(); 
        $("#selbook_name").toggle(); 
    }
    x =x +1;

    var target = event.target || event.srcElement;
    document.getElementById('selbook_name').innerHTML = event.target.innerHTML;
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
            $(".thumbnails").append("<li><a href = '"+dir+splitimg[i]+"' data-standard = '"+dir+splitimg[i]+"'><img src="+dir+splitimg[i]+" onclick = getName('"+splitimg[i]+"') width = 140px height = 120px></a><br>"+splitimg[i]+"</li>"); 


        }
    //    $(".selected_img").css("width", $('.selected_img').width() - 220+"px");
    });

    request.fail(function(jqXHR, textStatus) {
        alert( "Request failed: " + textStatus );
    });
} 

function segment_scannedimages(para)
{
    // $("#navr h2").toggle(); 
    $("#navr h2").html("Results")
        var source1=document.getElementById("selected_img").src;
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
        .select("#status")
        //.select(".easyzoom easyzoom--overlay easyzoom--with-thumbnails")

        // .select("#atag")
        //.select("#selected_img")
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
    var source1=document.getElementById("selected_img").src;


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
        .select("#status")
        //.select(".easyzoom easyzoom--overlay easyzoom--with-thumbnails")

        // .select("#atag")
        //.select("#selected_img")
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

    var book= document.getElementById('selbook_name').innerHTML;
    var image=document.getElementById("selected_img").src;

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

