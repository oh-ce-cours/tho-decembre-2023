#include <stdio.h>
#include <stdlib.h>

void format_hello(char* res, char* name, uint size){
	snprintf(res, size-1, "Hello %s !\n", name);
}