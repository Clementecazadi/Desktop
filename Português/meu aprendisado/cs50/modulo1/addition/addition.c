#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int x = get_int("Forneça o x: ");
    int y = get_int("Forneça o y: ");
    printf("%i\n", x + y);
}