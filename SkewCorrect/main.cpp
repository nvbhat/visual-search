#include "SkewCorrect.h"
#include <iostream>
using namespace std;

int main(int argc, char **argv)
{
	if (argc < 3)
	{
		cout << "Usage:./SkewCorrect [path-to-document-image] [path-to-skew-corrected-document-image] [skew-correction-result-file](optional)\n";
		return -1;
	}
	SkewCorrect skewCorrecter;
	
	skewCorrecter.Process(argv[1], argv[2]);

	return 0;
}