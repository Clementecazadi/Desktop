#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main(void)
{
    string v = get_string("Inpout: ");
    string s = "Olá mundo.";
    for (int c = 0, n = strlen(v); c < n; c++)
    {
        printf("%c\n", v[c]);
    }
    printf("%s %li\n", v, strlen(v));
}
