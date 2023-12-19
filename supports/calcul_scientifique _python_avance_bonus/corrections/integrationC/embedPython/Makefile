CC = gcc
CFLAGS = $(shell python-config --cflags --embed)
LDFLAGS = $(shell python-config --ldflags --embed)


simple.o: simple.c
	$(CC)  -c simple.c -o simple.o $(CFLAGS)

simple_error.o: simple_error.c
	$(CC)-c simple_error.c -o simple_error.o  $(CFLAGS) 

run_script.o: run_script.c
	$(CC)  -c run_script.c -o run_script.o $(CFLAGS)

run_script_string.o: run_script.c
	$(CC)  -c run_script_string.c -o run_script_string.o $(CFLAGS)


simple: simple.o
	$(CC) simple.o $(LDFLAGS) -o simple
	./simple

simple_error: simple_error.o
	$(CC) simple_error.o $(LDFLAGS) -o simple_error
	./simple_error

run_script: run_script.o
	$(CC) run_script.o $(LDFLAGS) -o run_script

run_script_string: run_script_string.o
	$(CC) run_script_string.o $(LDFLAGS) -o run_script_string




.PHONY : clean
clean :
	rm -f *.o simple simple_error run_script