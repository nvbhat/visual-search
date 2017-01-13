#include "DocumentImageViewer.h"
#include <iostream>
using namespace std;

int main(int argc, char **argv)
{
	if (argc != 3)
	{
		cout << "Usage:./DocumentImageViewer [path-to-document-image] [path-to-bounding-box-file]\n";
		return -1;
	}
	DocumentImageViewer viewer;
	
	viewer.ViewBoundingBoxes(argv[1], argv[2]);

	return 0;
}