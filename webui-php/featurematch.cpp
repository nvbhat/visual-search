/**

 * @file SURF_FlannMatcher
 * @brief SURF detector + descriptor + FLANN Matcher
 * Milan
 */

#include <stdio.h>
#include <iostream>
#include<string>
#include<fstream>
#include "opencv2/core/core.hpp"
#include "opencv2/features2d/features2d.hpp"
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/nonfree/features2d.hpp"

using namespace cv;
using namespace std;

/**
 * @function main
 * @brief Main function
 */
int main( int argc, char** argv )
{
  
  //Mat img_1 = imread( argv[1], CV_LOAD_IMAGE_GRAYSCALE );
  //Mat img_2 = imread( argv[2], CV_LOAD_IMAGE_GRAYSCALE );
  Mat img_1 = imread( argv[1]);
 
  Mat img_gray=imread(argv[1],CV_LOAD_IMAGE_GRAYSCALE);
  Mat img_2=imread(argv[2]);
  Mat gray_temp = imread( argv[2],CV_LOAD_IMAGE_GRAYSCALE);
 
  string book=string(argv[3]);
  ofstream myfile;
  //myfile.open(book.c_str());
  //cout << "width= " << img_2.size().width << " height= " << img_2.size().height << endl;
 
  
   //draw-circle parameters
    int width=img_2.size().width ;
    int height=img_2.size().height;
    int thickness = 3;
    int lineType  = 8;
    

  Mat m_docImage=img_1;
  if( !img_gray.data || !gray_temp.data )
  { std::cout<< " --(!) Error reading images " << std::endl; return -1; }
  cout << "dims 1 : " << img_gray.rows << " " << img_gray.cols << " channels:" << img_gray.channels() << endl;
  cout << "dims 2 : " << gray_temp.rows << " " << gray_temp.cols << endl;

  //-- Step 1: Detect the keypoints using SURF Detector
  int minHessian = 400;

  SurfFeatureDetector detector( minHessian );

  std::vector<KeyPoint> keypoints_1, keypoints_2;

  detector.detect( img_gray, keypoints_1 );
  detector.detect( gray_temp, keypoints_2 );

  cout << "Num keypoints 1 = " << keypoints_1.size() << endl;
  cout << "Num keypoints 2 = " << keypoints_2.size() << endl;

  //-- Step 2: Calculate descriptors (feature vectors)
  SurfDescriptorExtractor extractor;


  Mat descriptors_1, descriptors_2;

  extractor.compute( img_gray, keypoints_1, descriptors_1 );
  extractor.compute( gray_temp, keypoints_2, descriptors_2 );

  //-- Step 3: Matching descriptor vectors using FLANN matcher
  FlannBasedMatcher matcher;
  std::vector< DMatch > matches;
  matcher.match( descriptors_1, descriptors_2, matches );

  double max_dist = 0; double min_dist = 200;

  //-- Quick calculation of max and min distances between keypoints
  cout<<"ROWS:"<<descriptors_1.rows<<endl;
  for( int i = 0; i < descriptors_1.rows; i++ )
  { double dist = matches[i].distance;
    if( dist < min_dist ) min_dist = dist;
    if( dist > max_dist ) max_dist = dist;
  }

  printf("-- Max dist : %f \n", max_dist );
  printf("-- Min dist : %f \n", min_dist );

  //-- Draw only "good" matches (i.e. whose distance is less than 2*min_dist,
  //-- or a small arbitary value ( 0.02 ) in the event that min_dist is very
  //-- small)
  //-- PS.- radiusMatch can also be used here.Will try this after the filtering of images are done
  std::vector< DMatch > good_matches;

  for( int i = 0; i < descriptors_1.rows; i++ )
  { if( matches[i].distance <= max(2*min_dist, 0.25) )
    { 
	    good_matches.push_back( matches[i]);
   
          // circle(img_1,matches[i],5.0,Scalar( 0, 0, 255),thickness,lineType );
   
    }
  }

  
  //-- Draw only "good" matches
  Mat img_matches;
  drawMatches( img_gray, keypoints_1, gray_temp, keypoints_2,
               good_matches, img_matches, Scalar::all(-1), Scalar::all(-1),
               vector<char>(),DrawMatchesFlags::NOT_DRAW_SINGLE_POINTS );

 // circle(img_1,good_matches,5.0,Scalar( 0, 0, 255),thickness,lineType );
  //-- Show detected matches
  //imshow( "Good Matches", img_matches );


  Mat out3 = Mat::zeros(img_gray.rows,img_gray.cols,CV_8UC3);
         vector<Mat> channels;
         channels.push_back(m_docImage);
         channels.push_back(m_docImage);
	 channels.push_back(m_docImage);
	 merge(channels,out3);
   
  for( int i = 0; i < (int)good_matches.size(); i++ )
  { printf( "-- Good Match [%d] Keypoint 1: %d  -- Keypoint 2: %d  \n", i, good_matches[i].queryIdx, good_matches[i].trainIdx );}
    //cout<<"Query-Index:->"<<good_matches[i].queryIdx<<endl; }
     for(int i = 0; i < good_matches.size(); i=i+2)
    {
	    Point point1 = keypoints_1[good_matches[i].queryIdx].pt;
            
          
           Point p1(point1.x-width,point1.y-(height/2));
           Point p2(point1.x,point1.y+(height/2));

	   Point p1_new(point1.x,point1.y);
           //cout<< p1<<":"<<p2<<endl;
	 //  cout<<point2.x<<endl;
          circle(img_1,p1_new,14.0,Scalar( 0, 0, 255),thickness,lineType );

           //rectangle(img_1,p1,p2,Scalar(255,0,255),1,CV_AA,0);
           //imshow("Good Match inside",img_1);     
     }
     //Point p3(100,0);
     //Point p4(200,50);
    //rectangle(img_1,p3,p4,Scalar(255,0,255),1,CV_AA,0);
    //imshow("Good Match",img_1); 
    imwrite("2_Origimg_flann.jpg",img_1);
    imwrite("match.jpg",img_matches);
  waitKey(0);

  return 0;
}


