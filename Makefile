output: server.o main.o
	g++ -g main.o -o tenj

server.o: server.cpp
	g++ -c -g server.cpp

main.o: main.cpp
	g++ -c -g main.cpp


clean:
	rm *.o tenj