<html>
<head>
<link href="default.css" rel="stylesheet" type="text/css" media="screen" />
        <link href="default.css" rel="stylesheet" type="text/css" media="screen" />
	<link rel="stylesheet" href="css/example.css" />
	<link rel="stylesheet" href="css/easyzoom.css" />
        
        <script type="text/javascript" src="../../js/d3.v2.js"></script>
         <script type="text/javascript" src="../../js/d3.v3.min.js"></script>
        <script type="text/javascript" src="../../js/d3.tip.v0.6.3.js"></script>

       <script src="https://code.jquery.com/jquery-1.10.2.min.js"></script>
	<script src="dist/easyzoom.js"></script>
<title>
Visual-Search Results
</title>
<style>
.full{

width : 1200px;
text-align : center;

}

#heading{
width : 1005px;
margin-left : 160px;
background : black;
font-size : 48px;
font-weight : bold;
text-align : center;
}
#image_area{

width : 1000px;
margin-left : 160px;
height : 550px;
}


</style>
</head>
<body>
<div class = "full">
<div id = "heading">Visual Search Results</div>
             <div id = "image_area">
		<div id="example">
			<div class="easyzoom easyzoom--overlay easyzoom--with-thumbnails">
				<a href = "../../first.png" id="atag">
					<img src="../../first.png" id="mainimg"  alt="" width="950" height="365" />
				</a>
			</div>
                       <!--  <center><span id = "demo"  name="imgname"> Current Image:</span></center>--> 
			<div class = "thumbimg">
                         <ul class="thumbnails">


<?php
//$path = getcwd();
//echo "This Is  Absolute Path: ";
//echo $path;
        include('../../config.php');
  $root_dir=$_SERVER['DOCUMENT_ROOT'].$data;
  $savedircropimg=$root_dir."/tmp/template-images/"; 
       //echo $savedircropimg;
       $set_threshold = $_POST["threshold"];
        //echo $set_threshold; 
       $my_array = array();
       
        session_start();
     
        $srcimage=$_SESSION['srcimage'];
        $book=$_SESSION['bookname'];
       
        $ext = substr($srcimage, strrpos($srcimage, '.') +1);
        $targ_w = $targ_h = 20;
        $jpeg_quality = 100;
        
         if ($ext == "jpg" || $ext == "jpeg")
         {

          $src = $srcimage;
          $img_r = imagecreatefromjpeg($src);
       
          $dst_r = ImageCreateTrueColor( $_POST['w'],$_POST['h'] );
          imagecopyresampled($dst_r,$img_r,0,0,$_POST['x'],$_POST['y'],$_POST['w'],$_POST['h'],$_POST['w'],$_POST['h']);        
        
          
          
          imagejpeg($dst_r,$savedircropimg."croppedimage.jpg",$jpeg_quality);
               
          $imgfile = basename($srcimage);          
          $splitstr=split(".jpg",$imgfile);
          $resultimg=$splitstr[0]."-result.jpg";
          $splitbookname=split(".json",$book);
          $jsonresultfile=$splitbookname[0]."-result.json";
          $searched_images_dir=$splitbookname[0];
          
           $tempimgjpg = $root_dir."/tmp/template-images/croppedimage.jpg";
         
              if($set_threshold=='')
            {
             //$th_val=0.7;
          //echo exec("python fuzzyimgsearch.py -j ../../maindirectory/$book -i $tempimg -b $jsonresultfile  ");
            echo exec("python ../../python-scripts/fuzzyimgsearch.py -j $book -i $tempimgjpg -b $jsonresultfile -t 0.7 -d $root_dir ");
         
             }

             else
             {
           echo exec("python ../../python-scripts/fuzzyimgsearch.py -j $book -i $tempimgjpg -b $jsonresultfile -t $set_threshold -d $root_dir ");
             }
         }
          
       

  
 
       

         if ($ext == "png")
         {

          $srcpng = $srcimage;
          $img_r_png = imagecreatefrompng($srcpng);
          $dst_r_png = ImageCreateTrueColor( $_POST['w'],$_POST['h'] );
	  imagecopyresampled($dst_r_png,$img_r_png,0,0,$_POST['x'],$_POST['y'],$_POST['w'],$_POST['h'],$_POST['w'],$_POST['h']);
          
         
	  imagepng($dst_r_png,$savedircropimg."croppedimage.png");

          $imgfile_png = basename($srcimage);
          $splitstr=split(".png",$imgfile_png);
          $resultimg=$splitstr[0]."-result.png";
          $splitbookname=split(".json",$book);
          $jsonresultfile=$splitbookname[0]."-result.json";
          $searched_images_dir=$splitbookname[0];
          $tempimgpng = $root_dir."/tmp/template-images/croppedimage.png";
                  
         //echo exec("python fuzzyimgsearch.py -j ../../maindirectory/$book -i $tempimg -b $jsonresultfile");
            if($set_threshold == '')
            {
             // $th_val=0.7;
          //echo exec("python fuzzyimgsearch.py -j ../../maindirectory/$book -i $tempimg -b $jsonresultfile  ");
            echo exec("python ../../python-scripts/fuzzyimgsearch.py -j $book -i $tempimgpng -b $jsonresultfile -t 0.7 -d $root_dir");
         
            }

             else
             {
            echo exec("python ../../python-scripts/fuzzyimgsearch.py -j $book -i $tempimgpng -b $jsonresultfile -t $set_threshold -d $root_dir ");
             }
       

          }


?>

   <?php
       /************code for display of searched result images***********/
       $folder = $root_dir."/tmp/searched-images/Template-Match/".$searched_images_dir."/";   
        $rel_folderpath=str_replace($_SERVER['DOCUMENT_ROOT'],"",$folder);
        // echo $rel_folderpath;
       $filetype = '*.'.'jpg';
       $files = glob($folder.$filetype);
       $count = count($files);
       if($files)
        {
          $count = count($files);
        
          for ($i=0;$i<$count;$i++)
         {
           $rel_imgpath=str_replace($_SERVER['DOCUMENT_ROOT'],"",$files[$i]);
           $resultimg_final =$rel_imgpath;
           
           $my_array[]=$resultimg_final;
           //echo $resultimg_final;
          //list($resultimg_final)=$my_array;
        ?>
			
                      
                         <?php 
                         echo '<li>';
                         //echo $files[$i];
                         echo '<a  href="'.$resultimg_final.'" data-standard = "'.$resultimg_final.'"><img src="'.$resultimg_final.'" alt=""  height = "120px" width = "140px" /></a><br>';

                         echo '</li>';  
                          ?>
		       

          <?php
          }
     
       }

       else
       {
          echo "No image files available";
       }
 ?>
      <?php
       $count_array=count($my_array);
      
      ?>
     
        
       <script>
               /*  var count_val="<?php echo $count_array; ?>";
                  //alert(count_val);
                  var resultimglist = <?php echo json_encode($my_array); ?>;
                   
                
                 for(var i=0; i<count_val;i++)
                 {
                    
               $(".thumbnails").append("<li><a href = '"+resultimglist[i]+"' data-standard = '"+resultimglist[i]+"'><img src="+resultimglist[i]+"  width = 140px height = 120px></a><br>"+resultimglist[i]+"</li>"); 
   
                 }*/
                 //alert(str);
                var $easyzoom = $('.easyzoom').easyZoom();

		// Get an instance API
		var api = $easyzoom.filter('.easyzoom--with-thumbnails').data('easyZoom');
                
                $(".thumbnails").on("click", "a", function(e) {
			var $this = $(this);
                           
			e.preventDefault();

			// Use EasyZoom's `swap` method
			api.swap($this.data("standard"), $this.attr("href"));
                       
                      source = $this.attr("href");
                     // document.getElementById("mainimg").src=source;
                       //document.getElementById("mainimg").src="s3.jpg";
                        $("#aaa").empty();      

                       });
   </script>

  
                           </ul>			
	</div>
	</div>
	</div>

</div>
</body>
</html>
