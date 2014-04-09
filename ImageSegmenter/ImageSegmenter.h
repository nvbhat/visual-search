#pragma once
#include <vector>
#include <string>
#include <utility>
#include <opencv2/core/core.hpp>
#include<iostream>
#include "ConfigParser.h"
using namespace cv;
using namespace std;

class ImageSegmenter 
{
	private:
		ConfigParser m_cfgParser;
		
		unsigned int m_min_inter_word_gap;
		unsigned int m_whiten_band_height;
		unsigned int m_whiten_band_width;
		
		string m_document_image_path, m_output_file_path;
		string m_output_level;

		double m_white_row_fill_factor;
		double m_white_col_fill_factor;
		
		bool m_do_dilation;
		unsigned int m_line_element_length;

		string m_processing_roi;
		unsigned int m_roi_tlx, m_roi_tly, m_roi_brx, m_roi_bry;

		Mat m_docImage;
		Mat m_docImageCopy;
		vector< pair<unsigned int, unsigned int> > m_lineBoundaries;
		vector< vector< pair<unsigned int, unsigned int> > > m_wordBoundaries;
				
		void ReadConfigParams();
		void PreprocessImage(Mat& img);
		void SplitIntoLines(const Mat& img);
		void SplitLinesIntoWords(const Mat& img);
		void SplitLine(const Mat& lineImg, vector< pair<unsigned int,unsigned int> >& wordBoundaries);  
		void SaveOutput(const string& output_type);		

		Mat GetLineElement();

	public:
		ImageSegmenter(const string& config_file_path);
		bool Process();
		
};
