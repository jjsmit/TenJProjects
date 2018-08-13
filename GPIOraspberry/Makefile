
output: main.o GPIOClass.o
	gcc main.o GPIOClass.o -o Awesomeprogram -lstdc++

main.o: main.cpp
	gcc -c main.cpp -lstdc++

GPIOClass.o: GPIOClass.h GPIOClass.cpp 
	gcc -c GPIOClass.cpp -lstdc++

clean:
	rm *.o output