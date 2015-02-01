
#include <stdio.h>

void hello(int n);

double dprod(double *x, int n);

void dcumsum(double *a, double *b, int n);

void
hello(int n)
{
    int i;
    
    for (i = 0; i < n; i++)
    {
        printf("C says hello\n");
    }
}


int main()
{
    hello(5);
}