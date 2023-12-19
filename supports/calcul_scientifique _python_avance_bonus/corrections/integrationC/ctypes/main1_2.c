#include <stdio.h>
#include <stdlib.h>
#include <dlfcn.h>

#define STR_LEN 40

void format_hello(char*, char*, uint);

int main(){
  char res[STR_LEN];
  format_hello(res, "Matthieu", STR_LEN-1);
  printf("%s\n", res);

  return EXIT_SUCCESS;
}