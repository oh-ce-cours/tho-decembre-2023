#include <stdio.h>
#include <stdlib.h>
#include <dlfcn.h>

#define STR_LEN 40

long factorielle(int);

int main(){
  printf("Factorielle 1: %d\n", factorielle(1));
  printf("Factorielle 2: %d\n", factorielle(2));
  printf("Factorielle 3: %d\n", factorielle(3));
  printf("Factorielle 4: %d\n", factorielle(4));
  printf("Factorielle 5: %d\n", factorielle(5));
  printf("Factorielle 6: %d\n", factorielle(6));
  printf("Factorielle 7: %d\n", factorielle(7));
  printf("Factorielle 8: %d\n", factorielle(8));

  return EXIT_SUCCESS;
}