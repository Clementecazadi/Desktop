#include <stdio.h>

//prototype
void swap(int *a, int *b);

int main(void)
{
    int x = 2;
    int y = 3;

    printf("X is %i and Y is %i.\n", x, y);
    swap(&x, &y);
    printf("X is %i and Y is %i.\n", x, y);
}

void swap(int *a, int *b)
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}