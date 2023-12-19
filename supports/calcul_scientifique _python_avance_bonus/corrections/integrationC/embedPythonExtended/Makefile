CC = gcc
CFLAGS = $(shell python-config --cflags --embed)
LDFLAGS = $(shell python-config --ldflags --embed)


simple.o: simple.c
	$(CC)  -c simple.c -o simple.o $(CFLAGS)


simple: simple.o
	$(CC) simple.o $(LDFLAGS) -o simple
	./simple



.PHONY : clean
clean :
	rm -f *.o simple