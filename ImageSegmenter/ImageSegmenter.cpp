#include "ImageSegmenter.h"
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/core/core.hpp>
#include <iostream>
#include<fstream>
#include<string>
using namespace std;
using namespace cv;
ImageSegmenter::ImageSegmenter()
{
	m_white_row_threshold = 0;
	m_white_row_fill_factor = 1.0;

	m_white_col_threshold = 0;
	m_white_col_fill_factor = 1.0;

	m_MIN_INTER_WORD_GAP = 5;
}

void ImageSegmenter::DisplayWordBoundaries(const string& wordBoundariesFile,string path)
{

	Mat out3 = Mat::zeros(m_docImage.rows,m_docImage.cols,CV_8UC3);
	vector<Mat> channels;
	channels.push_back(m_docImage);
	channels.push_back(m_docImage);
	channels.push_back(m_docImage);
	merge(channels,out3);
        ofstream resultFile;

        cout<<"{"<<endl<<"\"imagepath\""<<": \""<<path<<"\","<<endl<<
                       "\"Segments\""<<":"<<"[";
          //resultFile.open("result_rect_layout.json");
         //  char path[50]="path to image ";
           // cout<<"{"<<endl<<"file"<<":"<<path<<","<<endl<<"}"<<endl;
	for(unsigned int i = 0 ; i < m_wordBoundaries.size() ; i++) {
		vector< pair<unsigned int,unsigned int> > wordBVec = m_wordBoundaries.at(i);
		pair<unsigned int,unsigned int> lineB = m_lineBoundaries.at(i);
		for(unsigned int j = 0 ; j < wordBVec.size() ; j++) {
			pair<unsigned int,unsigned int> wordB = wordBVec.at(j);
          
			if((i+j)>0)
				printf(",");
			printf("\n    { 'geometry': { 'x': %d, 'y': %d, 'width': %d, 'height': %d } }",
				wordB.first, lineB.first, 
				(wordB.second - wordB.first), (lineB.second - lineB.first));
				
			Point p1(wordB.first,lineB.first);
			Point p2(wordB.second,lineB.second);
                       cout<<p1<<p2<<endl;
			rectangle(out3,p1,p2,Scalar(255,0,255),1,CV_AA,0);
		}
	}

         cout<<endl<<"]"<<endl<<"}"<<endl;
          // resultFile.close();		
	imwrite(wordBoundariesFile.c_str(),out3);
      //  imshow("result image:",out3);
       // cout<<wordBoundariesFile.c_str()<<endl;
}


void ImageSegmenter::SplitIntoWords(const Mat& img,string& wordBoundariesFile,string path)
{
	SplitIntoLines(img);	
	SplitLinesIntoWords(img);
	DisplayWordBoundaries(wordBoundariesFile,path);
} 

void ImageSegmenter::SplitIntoLines(const Mat& img)
{
	m_docImage = img;
	//cout << " Rows = " << img.rows << "Cols = " << img.cols << endl;
             //cv::imshow("image",m_docImage);
	// Convert input grayscale image to binary image
	threshold(img,m_docImage,0,255,CV_THRESH_OTSU);
          	imwrite("binary-thresholded.png",m_docImage);
                // imshow("result",m_docImage);_          
	// Form row histogram of sum-across-columns
	vector<unsigned int> rowSums(img.rows,0);
	unsigned int rowSum =0;
	for(unsigned int row = 0; row < img.rows; ++row) {
		rowSum =0;
		for(unsigned int col = 0; col < img.cols; ++col)
			rowSum += m_docImage.at<unsigned char>(row,col);
		rowSums.at(row) = rowSum/255;
		//cout << "Row = " << row << " RowSum = " << rowSums.at(row) << endl;
	}

	// If an entry in the row histogram equals number of image columns,
	// it is considered a white line. Any other count for the entry
	// implies it is part of a text line in the document. We scan the row
	// histogram from top to bottom looking for transitions from white line
	// to text and vice-versa.
	m_white_row_threshold = static_cast<unsigned int>(static_cast<double>(img.cols) * m_white_row_fill_factor);
	//cout << "#Cols= " << img.cols << " Threshold=" << m_white_row_threshold << endl;
	unsigned int lineTop,lineBottom;

	Mat out3 = Mat::zeros(img.rows,img.cols,CV_8UC3);
	vector<Mat> channels;
	channels.push_back(m_docImage);
	channels.push_back(m_docImage);
	channels.push_back(m_docImage);
	merge(channels,out3);

	for(unsigned int i = 1 ; i < rowSums.size() ;i++) {
		//cout << "Rowsums: prev[" <<  rowSums.at(i-1) << "] curr[" << rowSums.at(i) << "]" << endl;
		if ( rowSums.at(i-1) >= m_white_row_threshold && rowSums.at(i) <= m_white_row_threshold ) 
			lineTop = i;
		else if ( rowSums.at(i-1) <= m_white_row_threshold && rowSums.at(i) >=  m_white_row_threshold ) {
			lineBottom = i;
			pair<unsigned int,unsigned int> lineB;
			lineB.first = lineTop;
			lineB.second = lineBottom;
			m_lineBoundaries.push_back(lineB);
			//cout << "Line: " << lineTop << " " << lineBottom << endl;
			// Draw and verify rectangle
			Point p1(0,lineTop);
			Point p2(img.cols-1,lineBottom);
			rectangle(out3,p1,p2,Scalar(255,0,255),1,CV_AA,0);
		}
	}
	//cout << "DONE\n";
	//imwrite("linerect.png",out3);
	//exit(1);

}		

void ImageSegmenter::SplitLinesIntoWords(const Mat& img)
{
	ofstream outfile;
        outfile.open("rectangle_result.txt");
	// Scan the line boundaries array and for each entry
	// split the line into words
	//cout << "Lines size=" << m_lineBoundaries.size() << endl;
	for(unsigned int i = 0 ; i < m_lineBoundaries.size() ; i++) {
		pair<unsigned int,unsigned int> currLineBoundaries = m_lineBoundaries.at(i);
		unsigned int currLineTop = currLineBoundaries.first;
		unsigned int currLineBottom = currLineBoundaries.second;
                
              //  outfile<<"Line:"<<currLineTop<<" "<<currLineBottom<<endl;
                
	     //cout << "Line: " << currLineTop << " " << currLineBottom << endl;
              // outfile<<"Rect [0,"<<currLineTop<<","<<m_docImage.cols<<","<<currLineBottom-currLineTop+1<<"]"<<endl;
	//cout << "Rect [0," << currLineTop << "," << m_docImage.cols << "," << currLineBottom-currLineTop+1 << "]" << endl; 
		Mat lineImg(m_docImage,cv::Rect(0,currLineTop,m_docImage.cols,currLineBottom-currLineTop+1));

		vector< pair<unsigned int,unsigned int> > wordBoundaries;
		SplitLine(lineImg,wordBoundaries);	
		m_wordBoundaries.push_back(wordBoundaries);
	}
         
		outfile.close();
}
