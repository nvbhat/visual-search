#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include<iostream>
#include<stdio.h>
using namespace std;
using namespace cv;

int main(int argc,char** argv) 
{
   //  cv::Mat ref = cv::imread("reference.png");
  //  cv::Mat tpl = cv::imread("template.png");
    cv::Mat ref=cv::imread(argv[1],1);
    cv::Mat tpl=cv::imread(argv[2],1);
   
    if (ref.empty() || tpl.empty())
        return -1;

     cv::Mat gref, gtpl;
     cv::cvtColor(ref, gref, CV_BGR2GRAY);
     cv::cvtColor(tpl, gtpl, CV_BGR2GRAY);
     cv::Mat res(ref.rows-tpl.rows+1, ref.cols-tpl.cols+1, CV_32FC1);
     cv::matchTemplate(gref, gtpl, res, CV_TM_CCOEFF_NORMED);
     cv::threshold(res, res, 0.7, 1.0, CV_THRESH_TOZERO);
           
       //cv:Scalar tempVal = mean( res ); 
      // float myMAtMean = tempVal.val[0];
      // cout<<"Avg:"<<myMAtMean<<endl;
    cv::imshow("Source Image",ref);
     
    cout<<"{"<<endl<<
        "\"imagepath\""<<": \""<<argv[1]<<","<<endl<<"\"template-imagepath\""<<": \""<<argv[2] <<"\","<<endl<< "\"Segments\""<<":"<<"[";
    int nMatches = 0;
     

    while (true) 
    {
        double minval, maxval, threshold = 0.7;
        cv::Point minloc, maxloc,ioi;
        cv::minMaxLoc(res, &minval, &maxval, &minloc, &maxloc);
        
        if (maxval >= threshold)
        {
              cv::rectangle(
                ref, 
                maxloc, 
                cv::Point(maxloc.x + tpl.cols, maxloc.y + tpl.rows),           
                CV_RGB(255,0,0),2
            );
           cv::floodFill(res, maxloc, cv::Scalar(0), 0, cv::Scalar(.1), cv::Scalar(1.));
          
         
       
       //printing the rectangle coordinates values  
     //   printf("x=%d,y=%d,xwidth=%d,yheight=%d\n",maxloc.x,maxloc.y,maxloc.x+tpl.cols,maxloc.y+tpl.rows);
        
           if (nMatches != 0)
           	printf(",");

           printf("\n    { 'geometry': { 'x': %d, 'y': %d, 'width': %d, 'height': %d } }",
                               maxloc.x, maxloc.y,
                               maxloc.x+tpl.cols,maxloc.y+tpl.rows);
   
    
           ++ nMatches;   
        }
        else
            break;
            
    }
     cout<<endl<<"]"<<endl<<"}"<<endl;
    cv::imwrite("result.jpg",ref);
    cv::imshow("Result Image", ref);
    cv::waitKey();
    return 0;

}
