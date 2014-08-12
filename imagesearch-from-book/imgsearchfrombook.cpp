#include <iostream>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/core/core.hpp>
#include<string>
#include <dirent.h>
#include<stdio.h>
#include<vector>
#include<fstream>
using namespace std;
using namespace cv;

   
 int main(int argc,char **argv)
 {
  

 
     string data="starting visual tool....";        
     cout<<data<<endl;
   
     char path_to_file[80]="./testimages/book-images/";
   
      vector<string> strVec;
      int max=20;
      Mat img_all[max];
      Mat gimg_all[max];
      vector<Mat>images;
    
      printf("files available are:\n");
      printf("\n");
               
       DIR *dir;
       struct dirent *file;
 
       string res;
       dir = opendir(path_to_file);
      
      if (dir != NULL){
       while (file = readdir(dir)){
      
       if(strcmp(file->d_name,".") != 0 && strcmp(file->d_name,"..")!=0)
        
     // printf("%s\n",epdf->d_name);
        res=file->d_name;
        strVec.push_back(res);
       

        }
     
     }
         //inputting template image
         cout<<"enter the template image..\n"<<endl;
         cv::Mat tempimg=cv::imread(argv[1],1); 
        // cv::imshow("Template Image",tempimg);
          cv::Mat gtempimg;
         cv::cvtColor(tempimg, gtempimg, CV_BGR2GRAY);
         //cv::imshow("Gray img",gtempimg);
         
          for (unsigned n=0; n<strVec.size(); ++n) {
          cout <<strVec.at( n ) << "\n";
        //sprintf(winName,"%d",n);//giving windows names
          string winName=strVec.at(n);
                
         img_all[n]=imread(path_to_file+strVec.at( n ),1);
         cv::cvtColor(img_all[n],gimg_all[n],CV_BGR2GRAY);
         cv::Mat res(img_all[n].rows-tempimg.rows+1, img_all[n].cols-tempimg.cols+1, CV_32FC1);
     
         cv::matchTemplate(gimg_all[n],gtempimg,res,CV_TM_CCOEFF_NORMED);
         cv::threshold(res, res, 0.7, 1.0, CV_THRESH_TOZERO);
          
          while(true)
         {
           double minval,maxval,threshold=.7;
           cv::Point minloc,maxloc,ioi;
           cv::minMaxLoc(res,&minval,&maxval,&minloc,&maxloc);

           if(maxval >= threshold)
          { 
               cv::rectangle(
               img_all[n],
               maxloc,
               cv::Point(maxloc.x + tempimg.cols, maxloc.y + tempimg.rows),
               CV_RGB(0,255,0),2
               );
             cv::floodFill(res, maxloc, cv::Scalar(0) ,0, cv::Scalar(.1),cv::Scalar(1.));
                 
           }
            else
              break;
     }
         
          
          imshow(winName,img_all[n]);
          
         
        
        }
          
        cv::waitKey(0);
             
     
   
      //cvNamedWindow("image", CV_WINDOW_AUTOSIZE);
      //cvShowImage("image",tempimg);

      

     return 0;
  }

   
