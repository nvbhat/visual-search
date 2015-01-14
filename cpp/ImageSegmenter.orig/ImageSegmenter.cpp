#include "ImageSegmenter.h"
#include <opencv2/imgproc/im gproc.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/core/core.hpp>
#include <iostream>

ImageSegmenter::ImageSegmenter(const string& config_file_path)
{	
	m_white_row_fill_factor = 0.99;	
	m_white_col_fill_factor = 1.0;

	m_min_inter_word_gap = 10; // A gap larger than this means we have a word

	m_whiten_band_height = 15;
	m_whiten_band_width = 15;

	m_do_dilation = false;
	m_line_element_length = 3;

	m_roi_tlx = m_roi_tly = m_roi_brx = m_roi_bry = 0;

	m_cfgParser.ReadParamFile(config_file_path);
	if (m_cfgParser.good())
		ReadConfigParams();
}

void ImageSegmenter::SaveOutput(const string& output_type)
{	

    Mat out = Mat::zeros(m_docImage.rows,m_docImage.cols,CV_8UC3);
	vector<Mat> channels;
	channels.push_back(m_docImage);
	channels.push_back(m_docImage);
	channels.push_back(m_docImage);
	merge(channels,out);

	ofstream ofs;
	ofs.open(m_output_file_path, ios::out);


	if (!ofs) {
		cerr << "Could not open output file " << m_output_file_path << " for writing\n";
		return;
	}

	vector<string> lines;
	if (output_type == "LINES") {
		for (unsigned int i = 0; i < m_lineBoundaries.size(); i++) {
			pair<unsigned int, unsigned int> lineB = m_lineBoundaries.at(i);
			stringstream ss;
			ss << 0 + m_roi_tlx << " " << lineB.first + m_roi_tly << " " << m_docImage.cols - 1 << " " << lineB.second + m_roi_tly;
			lines.push_back(ss.str());
			ss.str("");			
		}			
	}
	else if (output_type == "WORDS") {
		for (unsigned int i = 0; i < m_wordBoundaries.size(); i++) {
			vector< pair<unsigned int, unsigned int> > wordBVec = m_wordBoundaries.at(i);
			pair<unsigned int, unsigned int> lineB = m_lineBoundaries.at(i);
			for (unsigned int j = 0; j < wordBVec.size(); j++) {
				pair<unsigned int, unsigned int> wordB = wordBVec.at(j);
				stringstream ss;
				ss << wordB.first + m_roi_tlx << " " << lineB.first + m_roi_tly << " " << wordB.second + m_roi_tlx << " " << lineB.second + m_roi_tly;
				lines.push_back(ss.str());
				ss.str("");
                               Point p1(wordB.first + m_roi_tlx,lineB.first + m_roi_tly);
                               Point p2(wordB.second + m_roi_tlx,lineB.second + m_roi_tly);
                               cv::rectangle(out,p1,p2,Scalar(255,0,255),1,CV_AA,0);
                               //imshow("Segmented Image", out);		
		               imwrite("Segment.jpg",out);
			}
		}
                               waitKey(0);
	}

	// http://stackoverflow.com/a/16330323/482389
	// remove the line begin with character '\n'   
	std::remove_if(lines.begin(), lines.end(), [](string &line) { return line[0] == '\n'; });
	// append newline to every line except last line  
	std::for_each(lines.begin(), lines.end() - 1, [](string &line) { line += '\n'; });
	// write lines to new file
	for (unsigned int i = 0; i < lines.size(); i++)
		ofs << lines.at(i);
	ofs.close();

}

bool ImageSegmenter::Process()
{
	// Check if we are working on full image or ROI
	if (m_processing_roi.length() > 0) { // ROI
		Mat inputImage = imread(m_document_image_path.c_str(), CV_LOAD_IMAGE_GRAYSCALE); // converts to grayscale if required
		stringstream ss(m_processing_roi);
		
		ss >> m_roi_tlx >> m_roi_tly >> m_roi_brx >> m_roi_bry;
		
		Rect roi(m_roi_tlx, m_roi_tly, m_roi_brx - m_roi_tlx + 1, m_roi_bry - m_roi_tly + 1);
		m_docImage = inputImage(roi);
		//imshow("roi", m_docImage);
		//waitKey();
	}
	else {
		// Read input image
		m_docImage = imread(m_document_image_path.c_str(), CV_LOAD_IMAGE_GRAYSCALE); // converts to grayscale if required
	}
	


	PreprocessImage(m_docImage);

	SplitIntoLines(m_docImage);	

	if (m_output_level == "LINES") {
		SaveOutput(m_output_level);
		return true;
	}
	else {
		SplitLinesIntoWords(m_docImage);
		SaveOutput(m_output_level);
	}
			
	return true;
}



void ImageSegmenter::PreprocessImage(Mat& img)
{
	// Convert input grayscale image to binary image
	threshold(img, m_docImage, 0, 255, CV_THRESH_OTSU);
	
	// 'White'-en a band around the image boundaries
	img(Rect(0, 0, img.cols, m_whiten_band_height)) = Scalar(255); 
	img(Rect(0, img.rows - m_whiten_band_height, img.cols, m_whiten_band_height)) = Scalar(255);
	img(Rect(0, 0, m_whiten_band_width, img.rows)) = Scalar(255);
	img(Rect(img.cols - m_whiten_band_width,0,m_whiten_band_width, img.rows)) = Scalar(255);
}


Mat ImageSegmenter::GetLineElement()
{
	Mat M = Mat::zeros(m_line_element_length, m_line_element_length, CV_8UC1);
	M(Rect(0, m_line_element_length / 2, m_line_element_length, 1)) = Scalar(1);
	return M.clone();
}

void ImageSegmenter::SplitIntoLines(const Mat& img)
{
	Mat processImg, dilated_img;
	if (m_do_dilation) {		
		Mat element = GetLineElement();
		dilated_img = img.clone();
		dilate(img, dilated_img, element);
		//imshow("before",img);
		//imshow("after", dilated_img);		
		//waitKey();
		processImg = dilated_img;
	}
	else
		processImg = img;
	
	// Form row histogram of sum-across-columns
	vector<unsigned int> rowSums(processImg.rows,0);
	unsigned int rowSum =0;
	for(unsigned int row = 0; row < processImg.rows; ++row) {
		rowSum =0;
		for(unsigned int col = 0; col < processImg.cols; ++col)
			rowSum += processImg.at<unsigned char>(row,col);
		rowSums.at(row) = rowSum/255;
		//cout << "Row = " << row << " RowSum = " << rowSums.at(row) << endl;
	}

	// If an entry in the row histogram exceeds a threshold,
	// it is considered a white line. Otherwise, the entry
	// implies it is part of a text line in the document. We scan the row
	// histogram from top to bottom looking for transitions from white line
	// to text and vice-versa.
	unsigned int white_row_threshold = static_cast<unsigned int>(static_cast<double>(processImg.cols) * m_white_row_fill_factor);
	unsigned int lineTop=0,lineBottom=0;
	
	for(unsigned int i = 1 ; i < rowSums.size() ;i++) {
		//cout << "Rowsums: prev[" <<  rowSums.at(i-1) << "] curr[" << rowSums.at(i) << "]" << endl;
		if ( rowSums.at(i-1) >= white_row_threshold && rowSums.at(i) <= white_row_threshold ) 
			lineTop = i;
		else if ( rowSums.at(i-1) <= white_row_threshold && rowSums.at(i) >=  white_row_threshold ) {
			lineBottom = i;

		pair<unsigned int,unsigned int> lineB;
		lineB.first = lineTop;
		lineB.second = lineBottom;
		m_lineBoundaries.push_back(lineB);
		//cout << "Line: " << lineTop << " " << lineBottom << endl;		
		}
	}
	
}		

void ImageSegmenter::SplitLinesIntoWords(const Mat& img)
{
	
	// Scan the line boundaries array and for each entry
	// split the line into words
	//cout << "Lines size=" << m_lineBoundaries.size() << endl;
	for(unsigned int i = 0 ; i < m_lineBoundaries.size() ; i++) {
		pair<unsigned int,unsigned int> currLineBoundaries = m_lineBoundaries.at(i);
		unsigned int currLineTop = currLineBoundaries.first;
		unsigned int currLineBottom = currLineBoundaries.second;
		//cout << "Line: " << currLineTop << " " << currLineBottom << endl;
		//cout << "Rect [0," << currLineTop << "," << m_docImage.cols << "," << currLineBottom-currLineTop+1 << "]" << endl; 
		Mat lineImg(m_docImage,cv::Rect(0,currLineTop,m_docImage.cols,currLineBottom-currLineTop+1));

		vector< pair<unsigned int,unsigned int> > wordBoundaries;
		SplitLine(lineImg,wordBoundaries);	
		m_wordBoundaries.push_back(wordBoundaries);
	}
		
}
