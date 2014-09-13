#include "SkewCorrect.h"
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>

SkewCorrect::SkewCorrect()
{
	m_min_num_intersections = 10;
	m_min_num_pts_on_line = 5;
	m_max_line_gap = 5;
	m_angle = 0;
}

void SkewCorrect::Process(const char* image_file_path, const char* skew_corrected_image_file_path)
{

	m_docImage = imread(image_file_path,CV_LOAD_IMAGE_GRAYSCALE); 
	if (m_docImage.data == NULL) {
		cerr << "Could not open image\n";
		return;
	}
	
	Mat binarized = m_docImage.clone();
	threshold(m_docImage, binarized, 0, 255, CV_THRESH_OTSU);
	
	cv::Size size = binarized.size();
	cv::bitwise_not(binarized, binarized);

	//cv::imshow(image_file_path, binarized);
	//cv::waitKey(0);

	m_min_num_pts_on_line = size.width / 5.0f;
	std::vector<cv::Vec4i> lines;
	cv::HoughLinesP(binarized, lines, 1, CV_PI / 180, m_min_num_intersections, m_min_num_pts_on_line, m_max_line_gap);

	cv::Mat disp_lines(size, CV_8UC1, cv::Scalar(0, 0, 0));
	double angle = 0.;
	unsigned nb_lines = lines.size();
	for (unsigned i = 0; i < nb_lines; ++i)
	{
		cv::line(disp_lines, cv::Point(lines[i][0], lines[i][1]),
			cv::Point(lines[i][2], lines[i][3]), cv::Scalar(255, 0, 0));
		angle += atan2((double)lines[i][3] - lines[i][1],
			(double)lines[i][2] - lines[i][0]);
	}
	angle /= nb_lines; // mean angle, in radians.
	
	std::cout << "Angle of skew = " << angle * 180 / CV_PI << std::endl;

	m_angle = angle * 180 / CV_PI;
	Mat rotated = rotateImage(binarized, NULL, Rect(0, 0, binarized.cols, binarized.rows), m_angle);
	
	//cv::imshow(image_file_path, disp_lines);
	//cv::waitKey(0);
	//cv::destroyWindow(image_file_path);
	//imshow("Original", binarized);
	//waitKey();
	cv::bitwise_not(rotated, rotated);

	imwrite(skew_corrected_image_file_path, rotated);

	//namedWindow("Original", WINDOW_NORMAL);
	//imshow("Original", m_docImage);

	//namedWindow("De-rotated", WINDOW_NORMAL);
	//imshow("De-rotated", rotated);
	//waitKey();
}