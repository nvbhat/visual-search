#include <iostream>
#include <string>
#include <opencv2/highgui/highgui.hpp>
#include "ImageSegmenter.h"

int main(int argc, char **argv)
{

	if ( argc != 4 )
	{
		cout << "Usage:./ImageSegmenter [path-to-image-file] [path-to-word-boundaries-image][path-to-json-file]\n"; 
		return -1;
	}

	// Read input
	cv::Mat docImage = imread(argv[1],CV_LOAD_IMAGE_GRAYSCALE);
	if( docImage.data == NULL ){
		cout << "Could not open image file [" << string(argv[1]) << "]\n";
		return -1;
	}else
    {
		//cout << "Read image file [" << string(argv[1]) << "] OK\n";
	
             string imgpath=string(argv[1]);
	string wordBoundariesFile = string(argv[2]);
         string jsonresultfile=string(argv[3]);
	ImageSegmenter imgSeg;
	// Process
        //imgSeg.GetImagePath(imgpath);
	imgSeg.SplitIntoWords(docImage,wordBoundariesFile,imgpath,jsonresultfile);	
	//cout << "DONE\n";
     }
 	return 0;
}
