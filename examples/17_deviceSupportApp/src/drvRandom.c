/* drvRandom.c */ 
#include <stdlib.h>
 
double drvRandom(double upper_limit)
{
    return random() * upper_limit / RAND_MAX;
}

