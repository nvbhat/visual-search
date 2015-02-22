#include<iostream>
#include<vector>
#include<string>
#include<utility>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/core/core.hpp>
#include "ImageSegmenter.h"
using namespace cv;
using namespace std;

 void ImageSegmenter::SplitLine(const Mat& img,vector < pair <unsigned int,unsigned int> > &WordBoundaries)
 {
    //imshow("img",img);
    // waitKey(0);
     

   //cout << img.rows << " " << img.cols << endl;
             
	/*
	// Compute expected position of sirorekha bar
	int maxRowSum = -1;
	unsigned int maxRowId=0;
	for(unsigned int row = 0; row < img.rows; ++row) {
		unsigned int rowSum =0;
		for(unsigned int col = 0; col < img.cols; ++col)
			rowSum += m_docImage.at<unsigned char>(row,col);
		if ( rowSum > maxRowSum ) {
			maxRowSum = rowSum;
			maxRowId = row;
		}
	}
	// Make the sirorekha bar continuous
	//img(Rect(0,maxRowId,img.cols,1)) = Mat::zeros(img.cols,1,CV_8UC1);		
	*/
         // cout<<"hello"<<endl;
	vector<unsigned int> col_sums(img.cols,0);
	unsigned int col_Sum=0;   
    
	for(unsigned int col=0;col<img.cols;++col) {
     		col_Sum=0;
       		for(unsigned int row=0;row<img.rows;++row) 
      			col_Sum +=img.at<unsigned char>(row,col);
        	col_sums.at(col)=col_Sum/255;
        }

	// If an entry in the column histogram equals number of image rows,
	// it is considered a white line. Any other count for the entry
	// implies it is part of a text line in the document. We scan the column 
	// histogram from left to right looking for transitions from white line
	// to text and vice-versa.
	m_white_row_threshold = static_cast<unsigned int>(static_cast<double>(img.rows) * m_white_col_fill_factor);
	//cout << "#Cols= " << img.rows << " Threshold=" << m_white_row_threshold << endl;
	unsigned int lineLeft,lineRight;
	Mat out3 = Mat::zeros(img.rows,img.cols,CV_8UC3);
	vector<Mat> channels;
	channels.push_back(img);
	channels.push_back(img);
	channels.push_back(img);
	merge(channels,out3);

	vector < pair<unsigned int,unsigned int> > WordBoundariesTemp;
	for(unsigned int i = 1 ; i < col_sums.size() ;i++) {
		//cout << "Colsums:" << i << " prev[" <<  col_sums.at(i-1) << "] curr[" << col_sums.at(i) << "]" << endl;
		if ( col_sums.at(i-1) >= m_white_row_threshold && col_sums.at(i) <= m_white_row_threshold ) 
			lineLeft = i;
		else if ( col_sums.at(i-1) <= m_white_row_threshold && col_sums.at(i) >=  m_white_row_threshold ) {
			lineRight = i;
			pair<unsigned int,unsigned int> lineB;
			lineB.first = lineLeft;
			lineB.second = lineRight;
			WordBoundariesTemp.push_back(lineB);
			//cout << "Line: " << lineLeft << " " << lineRight << endl;
			// Draw and verify rectangle
			Point p1(lineLeft,0);
			Point p2(lineRight,img.rows-1);
			rectangle(out3,p1,p2,Scalar(255,0,255),1,CV_AA,0);
				
		}
	}
	//imwrite("linerect-row.png",out3);
	//exit(1);

	// Scan the word boundaries and retain only those which have a big width
	unsigned int currId = 0;
	unsigned int wordBegin=0,wordEnd=0;

	wordBegin = WordBoundariesTemp.at(0).first;
	while( currId < WordBoundariesTemp.size()-1 ) {
		unsigned int cwB = WordBoundariesTemp.at(currId).first;
		unsigned int cwE = WordBoundariesTemp.at(currId).second;
		unsigned int nwB = WordBoundariesTemp.at(currId+1).first;
		unsigned int nwE = WordBoundariesTemp.at(currId+1).second;
		unsigned int gap = nwB - cwE + 1;
		if ( gap > m_MIN_INTER_WORD_GAP ) {
			pair<unsigned int,unsigned int> wordB;
			wordB.first = wordBegin;
			wordB.second = cwE;
			WordBoundaries.push_back(wordB);
			wordBegin = nwB;
		}
		++currId;
	}
	
	pair<unsigned int,unsigned int> wordB = WordBoundariesTemp.at(WordBoundariesTemp.size()-1);
         
	WordBoundaries.push_back(wordB);

       /*for(int i=0;i<WordBoundaries.size();i++)
	         {
	cout<<"WB[ist]:-->"<<WordBoundaries[i].first<<" "<<"WB[2nd]:-->"<<WordBoundaries[i].second<<endl;
	          }*/


         
 }

