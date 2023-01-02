#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>

int main (void)
{
    string words[2];
    words[0] = "clemente";
    words[1] = "cazadi";
    for (int i = 0, n = strlen(words[1]); i < n; i++)
    {
        printf("%c", toupper(words[1][i]));
    }
    printf("\n");
}