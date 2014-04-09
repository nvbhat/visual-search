CFLAGS = `pkg-config --cflags opencv`
#LIBS = `pkg-config --libs opencv` -L/home/gopinath/opencv-2.4.8/release/lib
LIBS = `pkg-config --libs opencv`
SRCS = main.cpp DocumentImageViewer.cpp
ImageSeg : 
	#g++ $(CFLAGS) $(SRCS) $(LIBS) -o ImageSeg
	g++ $(SRCS) -o DocumentImageViewer $(CFLAGS) $(LIBS) 

clean: 
	rm -rf DocumentImageViewer
