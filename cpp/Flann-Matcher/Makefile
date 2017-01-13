CFLAGS = `pkg-config --cflags opencv` -std=c++0x
#LIBS = `pkg-config --libs opencv` -L/home/gopinath/opencv-2.4.8/release/lib
LIBS = `pkg-config --libs opencv`
SRCS = featurematch.cpp
Featuredetection : 
	#g++ $(CFLAGS) $(SRCS) $(LIBS) -o ImageSeg
	g++ $(SRCS) -o Featuredetection $(CFLAGS) $(LIBS) 

clean: 
	rm -f Featuredetection

