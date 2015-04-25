<?php

        
        session_start();
       // $text=$_SESSION['text'];
        //echo $text;
        $srcimage=$_SESSION['srcimage'];
       
        $dir = "../../visual-search/images/user-upload/";
       // echo $srcimage;
        $ext = substr($srcimage, strrpos($srcimage, '.') + 1);
        $targ_w = $targ_h = 20;
        $jpeg_quality = 100;
        
         if ($ext == "jpg")
         {
        $src = $dir.$srcimage;
        $img_r = imagecreatefromjpeg($src);
        //$dst_r = ImageCreateTrueColor( $targ_w, $targ_h );
         $dst_r = ImageCreateTrueColor( $_POST['w'],$_POST['h'] );

        //imagecopyresampled($dst_r,$img_r,0,0,$_POST['x'],$_POST['y'],
        //$targ_w,$targ_h,$_POST['w'],$_POST['h']);
        
         imagecopyresampled($dst_r,$img_r,0,0,$_POST['x'],$_POST['y'],$_POST['w'],$_POST['h'],$_POST['w'],$_POST['h']);        
        
          $savedircropimg="../../visual-search/images/template-images/";
       //  header('Content-type: image/jpeg');
         imagejpeg($dst_r,$savedircropimg."croppedimgtest3.jpg",$jpeg_quality);
                
        
          
       
        $splitstr=split(".jpg",$srcimage);
        $resultimg=$splitstr[0]."-result.jpg";
        $jsonresultfile=$splitstr[0]."-result.json";
        $outimgpathjpg="../../visual-search/images/searched-images/";
        
        $tempimg="../../visual-search/images/template-images/croppedimgtest3.jpg";
              
       // $tempimg="../../visual-search/images/template-images/durgachalisa_template.jpg";
        
         exec("../.././imgsearch $src  $tempimg ../../visual-search/books/searched-books/$jsonresultfile ../../visual-search/images/searched-images/$resultimg");
         }
          
        ?>

<!-- jjjjjjj-->     
 
        <?php

         if ($ext == "png")
         {
          $srcpng = $dir.$srcimage;
          $img_r_png = imagecreatefrompng($srcpng);
          $dst_r_png = ImageCreateTrueColor( $_POST['w'],$_POST['h'] );
	  imagecopyresampled($dst_r_png,$img_r_png,0,0,$_POST['x'],$_POST['y'],$_POST['w'],$_POST['h'],$_POST['w'],$_POST['h']);
          $savedircropimg_png="../../visual-search/images/template-images/";
	  imagepng($dst_r_png,$savedircropimg_png."croppedimgtest3.png");
          
         $splitstr=split(".png",$srcimage);
         $resultimg=$splitstr[0]."-result.png";
         $jsonresultfile=$splitstr[0]."-result.json";
         $outimgpathjpg="../../visual-search/images/searched-images/";

         $tempimg="../../visual-search/images/template-images/croppedimgtest3.png";          
          exec("../.././imgsearch $srcpng  $tempimg ../../visual-search/books/searched-books/$jsonresultfile ../../visual-search/images/searched-images/$resultimg");

       
//echo "hello";

          }


?>

  <img src = <?php echo $outimgpathjpg.$resultimg ?>  height="500" width="500">

