#pragma once
#include <iostream>
#include <fstream>
#include <opencv2/core/core.hpp>

using namespace std;
using namespace cv;

class DocumentImageViewer {
private:
	Mat m_docImage;
public:
	void ViewBoundingBoxes(const char* image_file_path, const char* bounding_box_file_path);
};