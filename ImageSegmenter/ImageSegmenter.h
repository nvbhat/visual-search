#pragma once
#include <vector>
#include <string>
#include <utility>
#include <opencv2/core/core.hpp>
#include<iostream>
using namespace cv;
using namespace std;

class ImageSegmenter 
{
	private:
		vector< pair<unsigned int,unsigned int> > m_lineBoundaries;
		vector< vector< pair<unsigned int,unsigned int> > > m_wordBoundaries;
		unsigned int m_white_row_threshold;
		double m_white_row_fill_factor;
		unsigned int m_white_col_threshold;
		double m_white_col_fill_factor;
		unsigned int m_MIN_INTER_WORD_GAP;
		Mat m_docImage;

		void SplitIntoLines(const Mat& img);
		void SplitLinesIntoWords(const Mat& img);
		void SplitLine(const Mat& lineImg, vector< pair<unsigned int,unsigned int> >& wordBoundaries);  
		void DisplayWordBoundaries(const string& wordBoundariesFile);
	public:
		ImageSegmenter();
		void SplitIntoWords(const Mat& img,string& wordBoundariesFile); 
};
