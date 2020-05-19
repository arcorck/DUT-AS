CXX = g++
CFLAGS=-g #pour pouvoir débugguer

all: ExeArtiste

ExeArtiste: Art.o Artiste.o Chanteur.o Acteur.o ExeArtiste.o
	@g++ $(CFLAGS) -Wall -o $@ $^

%.o: %.cpp %.hpp
	$(CXX) $(CFLAGS) -Wall -c $<

%.o: %.cpp
	$(CXX) $(CFLAGS) -Wall -c $<


clean:
	rm *.o ExeArtiste


