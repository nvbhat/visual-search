#include "DocumentImageViewer.h"
#include <opencv2/highgui/highgui.hpp>

void DocumentImageViewer::ViewBoundingBoxes(const char* image_file_path, const char* bounding_box_file_path)
{
	m_docImage = imread(image_file_path); 
	if (m_docImage.data == NULL) {
		cerr << "Could not open image\n";
		return;
	}
		

	ifstream ifs;
	ifs.open(bounding_box_file_path, ios::in);
	if (!ifs) {
		cerr << "Could not open " << bounding_box_file_path << " for reading.\n";
		return;
	}
	string line;
	while (getline(ifs, line)) {
		if (*line.rbegin() == '\r')
			line.erase(line.length() - 1);
		istringstream iss(line);
		unsigned int tlx, tly, brx, bry;
		iss >> tlx >> tly >> brx >> bry;
		Point p1(tlx, tly);
		Point p2(brx, bry);
		rectangle(m_docImage, p1, p2, Scalar(255, 0, 255), 1, CV_AA, 0);
	}
	ifs.close();

	imshow("Bounding Boxes", m_docImage);
	waitKey();
}