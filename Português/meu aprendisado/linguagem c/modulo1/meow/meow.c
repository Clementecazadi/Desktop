#include <stdio.h>

// Prototipe
void meow();

int main(void)
{
    meow(5);
}

// Custum Function
void meow(int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("Hello world\n");
    }
}