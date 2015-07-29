CFLAGS = `pkg-config --cflags opencv` -std=c++0x
#LIBS = `pkg-config --libs opencv` -L/home/gopinath/opencv-2.4.8/release/lib
LIBS = `pkg-config --libs opencv`
SRCS = main.cpp ConfigParser.cpp ImageSegmenter.cpp ReadConfigParams.cpp SplitLine.cpp
ImageSegmenter : 
	#g++ $(CFLAGS) $(SRCS) $(LIBS) -o ImageSeg
	g++ $(SRCS) -o ImageSegmenter $(CFLAGS) $(LIBS) 

clean: 
	rm -f ImageSegmenter
