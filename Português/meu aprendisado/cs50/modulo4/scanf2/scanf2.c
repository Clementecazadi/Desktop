#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>

int main(void)
{
    //char s[4];
    char *s;
    s = malloc(4);
    printf("Digite algo: ");
    scanf("%s", s);
    printf("%s\n", s);
    free(s);
}