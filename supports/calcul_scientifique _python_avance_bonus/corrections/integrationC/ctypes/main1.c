#include <stdio.h>
#include <stdlib.h>
#include <dlfcn.h>

#define STR_LEN 40

int main(){
  void* test1_lib;
  void (*format_hello)(char*, char*, uint);

  test1_lib = dlopen("./libtest1.so", RTLD_LAZY);
  if ( test1_lib == NULL )
    fprintf((stderr), "Error opening the library\n");

  *(void **)(&format_hello) = dlsym(test1_lib, "format_hello");

  char res[STR_LEN];
  format_hello(res, "Matthieu", STR_LEN-1);
  printf("%s\n", res);

  return EXIT_SUCCESS;
}