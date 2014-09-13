#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include <iostream>
#include <stdio.h>

using namespace std;
using namespace cv;

int main(int argc ,char **argv)
{

 Mat inImage = imread (argv[1], 0);
       cv::Mat binaryImage = inImage.clone();
      cv::threshold(inImage, binaryImage, 0, 255, CV_THRESH_OTSU);
       imshow("Bin-Threshold Image",binaryImage);
       waitKey();
       cout<<"Done";
       //cv::Mat outImage = cv::Mat::zeros( inImage.rows, inImage.cols,inImage.type() );
         //  inImage.copyTo(outImage, binaryImage );
                  // imshow("Result", outImage);
                  Mat outimg=imwrite(binaryImage);
      

                   cout<<"Again";
                   return 0;
                   }
                   
