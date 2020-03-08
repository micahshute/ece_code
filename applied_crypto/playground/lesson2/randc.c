#include "stdio.h"
#include "stdlib.h"

int main(void) {

    unsigned int seed = 1;
    srand(seed);

    int i=0;
    for(; i < 5; i++){
      printf(" %u ", rand());
    }

    return 0;
}