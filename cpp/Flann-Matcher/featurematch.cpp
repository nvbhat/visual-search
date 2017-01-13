/**
 * @file SURF_FlannMatcher
 * @brief SURF detector + descriptor + FLANN Matcher
 * @author A. Huaman
 */

#include <stdio.h>
#include <iostream>
#include "opencv2/core/core.hpp"
#include "opencv2/features2d/features2d.hpp"
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/nonfree/features2d.hpp"

using namespace cv;
using namespace std;

void readme();

/**
 * @function main
 * @brief Main function
 */
int main( int argc, char** argv )
{
  if( argc != 3 )
  { readme(); return -1; }

  //Mat img_1 = imread( argv[1], CV_LOAD_IMAGE_GRAYSCALE );
  //Mat img_2 = imread( argv[2], CV_LOAD_IMAGE_GRAYSCALE );
   Mat img_1 = imread( argv[1] );
  Mat img_2 = imread( argv[2]);

  //cout << "width= " << img_2.size().width << " height= " << img_2.size().height << endl;
  int width=img_2.size().width ;
  int height=img_2.size().height;

  Mat m_docImage=img_1;
  if( !img_1.data || !img_2.data )
  { std::cout<< " --(!) Error reading images " << std::endl; return -1; }
  cout << "dims 1 : " << img_1.rows << " " << img_1.cols << " channels:" << img_1.channels() << endl;
  cout << "dims 2 : " << img_2.rows << " " << img_2.cols << endl;

  //-- Step 1: Detect the keypoints using SURF Detector
  int minHessian = 400;

  SurfFeatureDetector detector( minHessian );

  std::vector<KeyPoint> keypoints_1, keypoints_2;

  detector.detect( img_1, keypoints_1 );
  detector.detect( img_2, keypoints_2 );

  cout << "Num keypoints 1 = " << keypoints_1.size() << endl;
  cout << "Num keypoints 2 = " << keypoints_2.size() << endl;

  //-- Step 2: Calculate descriptors (feature vectors)
  SurfDescriptorExtractor extractor;


  Mat descriptors_1, descriptors_2;

  extractor.compute( img_1, keypoints_1, descriptors_1 );
  extractor.compute( img_2, keypoints_2, descriptors_2 );

  //-- Step 3: Matching descriptor vectors using FLANN matcher
  FlannBasedMatcher matcher;
  std::vector< DMatch > matches;
  matcher.match( descriptors_1, descriptors_2, matches );

  double max_dist = 0; double min_dist = 100;

  //-- Quick calculation of max and min distances between keypoints
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
  { if( matches[i].distance <= max(2*min_dist, 0.10) )
    { good_matches.push_back( matches[i]); }
  }

  
  //-- Draw only "good" matches
  Mat img_matches;
  drawMatches( img_1, keypoints_1, img_2, keypoints_2,
               good_matches, img_matches, Scalar::all(-1), Scalar::all(-1),
               vector<char>(), DrawMatchesFlags::NOT_DRAW_SINGLE_POINTS );

  //-- Show detected matches
  imshow( "Good Matches", img_matches );


  Mat out3 = Mat::zeros(img_1.rows,img_1.cols,CV_8UC3);
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
           // cout<< point1.x<<endl;
	    //Point2f point2 = keypoints_2[good_matches[i].trainIdx].pt;
	    //Point2f point3 = keypoints_1[good_matches[i].trainIdx].pt;
	    //Point2f point4 = keypoints_2[good_matches[i].queryIdx].pt;
            // do something with the best points...
               //cout<<point1<<endl;
           // cout<<"point p1:"<<point1<<endl;
           //rectangle(img_1,point1,point2,Scalar(255,0,255),1,CV_AA,0);
           Point p1(point1.x-width,point1.y-(height/2));
           Point p2(point1.x,point1.y+(height/2));
           cout<< p1<<":"<<p2<<endl;
    
            rectangle(img_1,p1,p2,Scalar(255,0,255),1,CV_AA,0);
           
     }
     //Point p3(100,0);
     //Point p4(200,50);
    //rectangle(img_1,p3,p4,Scalar(255,0,255),1,CV_AA,0);
    imshow("Good Match",img_1); 
  imwrite("match.jpg",img_matches);
  waitKey(0);

  return 0;
}

/**
 * @function readme
 */
void readme()
{ std::cout << " Usage: ./SURF_FlannMatcher <img1> <img2>" << std::endl; }

