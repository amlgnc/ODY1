all: compile link run

compile:
	g++ -c src/main.cpp -Iinclude -o bin/main.o

link:
	g++ bin/main.o -o bin/main -Llib -lsfml-graphics -lsfml-window -lsfml-system

run:
	./bin/main