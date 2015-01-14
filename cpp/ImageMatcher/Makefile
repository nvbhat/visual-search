CFLAGS = `pkg-config --cflags opencv`
LIBS = `pkg-config --libs opencv` #-L/home/gopinath/opencv-2.4.8/release/lib
SRCS =imgsearch.cpp
PGM =imgsearch

${PGM} : 
	g++ $(CFLAGS) $(SRCS) $(LIBS) -o $@

clean: 
	rm -rf ${PGM}
