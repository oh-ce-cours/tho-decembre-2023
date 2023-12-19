test1.so: test1.c
	gcc -shared -o libtest1.so -fPIC -Wall test1.c

main1: main1.c test1.so
	gcc main1.c -Wall -ldl -o main


main1_2: main1_2.c test1.so
	gcc main1_2.c -Wall -ltest1 -L. -o main1_2


test2.so: test2.c
	gcc -shared -o libtest2.so -fPIC -Wall test2.c

main2: main2.c test2.so
	gcc main2.c -Wall -ltest2 -L. -o main2
