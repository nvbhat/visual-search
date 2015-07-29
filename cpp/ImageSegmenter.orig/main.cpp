#include <iostream>
#include <string>
#include "ImageSegmenter.h"
#include "ConfigParser.h"

int main(int argc, char **argv)
{
	if ( argc != 2 )
	{
		cout << "Usage:./ImageSegmenter [path-to-config-file]\n"; 
		return -1;
	}
	
	ImageSegmenter imageSegmenter(argv[1]);
	
	imageSegmenter.Process();
		
	cout << "DONE\n";

	return 0;
	
}
