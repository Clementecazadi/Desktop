#include <stdio.h>
#include <string.h>
#include <cs50.h>

int main(void)
{
    char *s = get_string("s: ");
    char *t = get_string("t: ");
    if (t == s)
    {
        printf("Igual\n");
    }
    else
    {
        printf("Diferente\n");
    }

    if (strcmp(s, t) == 0)
    {
        printf("Igual\n");
    }
    else
    {
        printf("Diferente\n");
    }
}