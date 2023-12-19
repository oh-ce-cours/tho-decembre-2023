#include "stdio.h"
#include "stdlib.h"
#include <math.h>
#include <stdint.h>
#include <string.h>

#define STRING_SIZE 50

void format_hello(char* res, char* name){
    strcat(res, name);
    strcat(res, " ! \n");
}


////////////////////////////////////////////////////

typedef struct {
   int   nb_eleves;
   int   nb_profs;
   char  prof[STRING_SIZE+1];
} Formation;


int get_nb_eleves(Formation *f){
    return f->nb_eleves;
}

int get_nb_profs(Formation *f){
    return f->nb_profs;
}

void get_nom_prof(Formation *f, char* buf){
    strncpy(buf, f->prof, STRING_SIZE);
}

////////////////////////////////////////////////////////:

float sinc(float x)
{
    return sinf(x) / x;
}


void sinc_1d(float* xs, float* res, int lenght){
    for(int i = 0; i < lenght; i++){
        res[i] = sinc(xs[i]);
    }
}


double somme_elements(double *A, int m, int n)
{
  // printf("reference 0,0 element\n");
  // printf("%f\n", A[0]);

  double somme = 0;
  for (int i = 0; i < m; i++)
  {
    for (int j = 0; j < n; j++)
      {
        // printf("%d, %d is %f\n", i, j, A[i*m + j]);
        somme += A[i*m + j];
      }
  }
  return somme;
}


int main(void/*int argc, char* argv[]*/){
    char hello[40] = "Hello ";
    format_hello(hello, "Matthieu");
    printf("%s", hello);

    printf("============ Struct ============\n");
    Formation f;
    f.nb_eleves = 10;
    strncpy(f.prof, "Matthieu Falce", STRING_SIZE);
    printf("Nb eleves : %d\n", get_nb_eleves(&f));

    char nom[50];
    get_nom_prof(&f, nom);
    printf("Prof : %s\n", nom);

    return 0;
}