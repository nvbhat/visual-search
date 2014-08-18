#include <iostream>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/core/core.hpp>
#include<string>
#include <dirent.h>
#include<stdio.h>
#include<vector>
#include<fstream>
#include<stdlib.h>

using namespace std;
using namespace cv;

void
findMatches(
        string img_path,
        string tempimg_path,
        Mat& tempimg,
        Mat& grey_tempimg,
        string winName
    )
{
	Mat img_all;
	Mat gimg_all;

    printf("{\n");
    printf("    \"imagepath\": \"%s\",\n", img_path.c_str());
    printf("    \"template-imagepath\": \"%s\",\n", tempimg_path.c_str());
    printf("    \"segments\": [\n");

    img_all = imread(img_path, 1);
    cvtColor(img_all,gimg_all,CV_BGR2GRAY);
    Mat res(img_all.rows-tempimg.rows+1, img_all.cols-tempimg.cols+1, CV_32FC1);

    matchTemplate(gimg_all,grey_tempimg,res,CV_TM_CCOEFF_NORMED);
    threshold(res, res, 0.7, 1.0, CV_THRESH_TOZERO);

    int nMatches = 0;
  
    while (true) {
        double minval,maxval,threshold=.7;
        Point minloc,maxloc,ioi;
        minMaxLoc(res,&minval,&maxval,&minloc,&maxloc);
        if (maxval >= threshold)
        { 
            rectangle(img_all, maxloc, 
                Point(maxloc.x + tempimg.cols, maxloc.y + tempimg.rows),
                CV_RGB(0,255,0),2);
            floodFill(res, maxloc, Scalar(0) ,0, Scalar(.1), Scalar(1.));
        
            if (nMatches != 0)
           	    printf(",");

            printf("\n    { 'geometry': { 'x': %d, 'y': %d, 'width': %d, 'height': %d } }",
                               maxloc.x, maxloc.y,
                               maxloc.x+tempimg.cols,maxloc.y+tempimg.rows);
    
           ++ nMatches;   
        }
        else
            break;
    }
    printf("}\n");
     
    imshow(winName,img_all);
}
   
int 
main(int argc, char **argv)
{
    string data="starting visual tool....";        
    cout<<data<<endl;
    cout<<"\n";
    
	char path_to_file[80]="./testimages/book-images/";
	char path_to_templateimage_file[80]="./testimages/template-images/";

	vector<string> imgfnames;
	int max=20;
	Mat img_all[max];
	Mat gimg_all[max];
	vector<string> tempimglist;
    // printf("files available are:\n");
    // printf("\n");
               
    DIR *dir;
    struct dirent *file;

    string res;
    dir = opendir(path_to_file);
      
    if (dir != NULL) {
        while (file = readdir(dir)) {
            if (strcmp(file->d_name, ".") && strcmp(file->d_name, "..")) {
                imgfnames.push_back(file->d_name);
            }
       }
    }
         
    printf("Template-image lists...\n");
       

    DIR *tempimgdir;
    struct dirent *tempimgfile;

    string tempimgres;
    tempimgdir = opendir(path_to_templateimage_file);

    if (tempimgdir != NULL) {
        while (tempimgfile = readdir(tempimgdir)) {
            if (strcmp(tempimgfile->d_name,".") && strcmp(tempimgfile->d_name,".."))
                tempimglist.push_back(tempimgfile->d_name);

        }
    }

    for (unsigned i=0; i<tempimglist.size(); ++i)
    {
        cout<<tempimglist.at(i)<<endl;
    }

    printf("enter the template image from the lists above to search....\n");
    string input_tempimg;
    cin>>input_tempimg;
    string input_tempimg_path=path_to_templateimage_file+input_tempimg;
    //  cout<<input_tempimg_path<<endl;
    Mat tempimg=imread(input_tempimg_path, 1);
    
            
    //inputting template image commnadline arguments
    // cout<<"enter the template image..\n"<<endl;
    // Mat tempimg=imread(argv[1],1); 
    // imshow("Template Image",tempimg);
    Mat gtempimg;
    cvtColor(tempimg, gtempimg, CV_BGR2GRAY);
     //imshow("Gray img",gtempimg);
     
    for (unsigned n=0; n<imgfnames.size(); ++n) {
        // cout <<imgfnames.at( n ) << "\n";
        //sprintf(winName,"%d",n);//giving windows names
        string winName=imgfnames.at(n);
            
        findMatches(path_to_file+imgfnames.at( n ), input_tempimg_path, 
                tempimg, gtempimg,winName);
    }
          
    waitKey(0);
             
    return 0;
}
