all: compile link run

compile:
	g++ -c src/main.cpp -ISFML/include -o SFML/bin/main.o

link:
	g++ SFML/bin/main.o -o SFML/bin/main -LSFML/lib -lsfml-audio -lsfml-graphics -lsfml-window -lsfml-system

run:
	./SFML/bin/main