output: server.o
	g++ -g server.o -o server

server.o: server.cpp
	g++ -c -g server.cpp


clean:
	rm *.o server