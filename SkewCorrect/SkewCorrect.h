#pragma once
#include <iostream>
#include <fstream>
#include <opencv2/core/core.hpp>
#include <opencv2/imgproc/imgproc.hpp>

using namespace std;
using namespace cv;

class SkewCorrect {
private:
	Mat m_docImage;
	int m_min_num_intersections;
	double m_min_num_pts_on_line;
	double m_max_line_gap;

	double m_angle;

	// http://stackoverflow.com/a/16159613/482389
	// ROTATE p by R
	/**
	* Rotate p according to rotation matrix (from getRotationMatrix2D()) R
	* @param R     Rotation matrix from getRotationMatrix2D()
	* @param p     Point2f to rotate
	* @return      Returns rotated coordinates in a Point2f
	*/
	Point2f rotPoint(const Mat &R, const Point2f &p)
	{
		Point2f rp;
		rp.x = (float)(R.at<double>(0, 0)*p.x + R.at<double>(0, 1)*p.y + R.at<double>(0, 2));
		rp.y = (float)(R.at<double>(1, 0)*p.x + R.at<double>(1, 1)*p.y + R.at<double>(1, 2));
		return rp;
	}

	//COMPUTE THE SIZE NEEDED TO LOSSLESSLY STORE A ROTATED IMAGE
	/**
	* Return the size needed to contain bounding box bb when rotated by R
	* @param R     Rotation matrix from getRotationMatrix2D()
	* @param bb    bounding box rectangle to be rotated by R
	* @return      Size of image(width,height) that will compleley contain bb when rotated by R
	*/
	Size rotatedImageBB(const Mat &R, const Rect &bb)
	{
		//Rotate the rectangle coordinates
		vector<Point2f> rp;
		rp.push_back(rotPoint(R, Point2f(bb.x, bb.y)));
		rp.push_back(rotPoint(R, Point2f(bb.x + bb.width, bb.y)));
		rp.push_back(rotPoint(R, Point2f(bb.x + bb.width, bb.y + bb.height)));
		rp.push_back(rotPoint(R, Point2f(bb.x, bb.y + bb.height)));
		//Find float bounding box r
		float x = rp[0].x;
		float y = rp[0].y;
		float left = x, right = x, up = y, down = y;
		for (int i = 1; i<4; ++i)
		{
			x = rp[i].x;
			y = rp[i].y;
			if (left > x) left = x;
			if (right < x) right = x;
			if (up > y) up = y;
			if (down < y) down = y;
		}
		int w = (int)(right - left + 0.5);
		int h = (int)(down - up + 0.5);
		return Size(w, h);
	}

	/**
	* Rotate region "fromroi" in image "fromI" a total of "angle" degrees and put it in "toI" if toI exists.
	* If toI doesn't exist, create it such that it will hold the entire rotated region. Return toI, rotated imge
	*   This will put the rotated fromroi piece of fromI into the toI image
	*
	* @param fromI     Input image to be rotated
	* @param toI       Output image if provided, (else if &toI = 0, it will create a Mat fill it with the rotated image roi, and return it).
	* @param fromroi   roi region in fromI to be rotated.
	* @param angle     Angle in degrees to rotate
	* @return          Rotated image (you can ignore if you passed in toI
	*/
	Mat rotateImage(const Mat &fromI, Mat *toI, const Rect &fromroi, double angle)
	{
		//CHECK STUFF
		// you should protect against bad parameters here ... omitted ...

		//MAKE OR GET THE "toI" MATRIX
		Point2f cx((float)fromroi.x + (float)fromroi.width / 2.0, fromroi.y +
			(float)fromroi.height / 2.0);
		Mat R = getRotationMatrix2D(cx, angle, 1);
		Mat rotI;
		if (toI)
			rotI = *toI;
		else
		{
			Size rs = rotatedImageBB(R, fromroi);
			rotI.create(rs, fromI.type());
		}

		//ADJUST FOR SHIFTS
		double wdiff = (double)((cx.x - rotI.cols / 2.0));
		double hdiff = (double)((cx.y - rotI.rows / 2.0));
		R.at<double>(0, 2) -= wdiff; //Adjust the rotation point to the middle of the dst image
		R.at<double>(1, 2) -= hdiff;

		//ROTATE
		warpAffine(fromI, rotI, R, rotI.size(), INTER_CUBIC, BORDER_CONSTANT, Scalar::all(0));

		//& OUT
		return(rotI);
	}
public:
	SkewCorrect();
	void Process(const char* image_file_path, const char* skew_corrected_image_file_path);
};