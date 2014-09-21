CFLAGS = `pkg-config --cflags opencv`
LIBS = `pkg-config --libs opencv`
SRCS = main.cpp SkewCorrect.cpp 
SkewCorrect : 
	g++ $(CFLAGS) $(SRCS) $(LIBS) -o SkewCorrect

clean: 
	rm -rf SkewCorrect
