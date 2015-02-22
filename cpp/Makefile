CFLAGS = `pkg-config --cflags opencv`
LIBS = `pkg-config --libs opencv` -L/home/gopinath/opencv-2.4.8/release/lib
SRCS = main.cpp ImageSegmenter.cpp SplitLine.cpp
ImageSeg : 
	g++ $(CFLAGS) $(SRCS) $(LIBS) -o ImageSeg

clean: 
	rm -f ImageSeg
