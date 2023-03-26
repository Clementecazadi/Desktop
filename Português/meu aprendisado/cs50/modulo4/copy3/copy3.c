#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    char *s = get_string("s: ");
    char *t = malloc(strlen(s));
    if (t == NULL)
    {
        return 1;
    }

    strcpy(t, s);

    if (strlen(t))
    {
        *t = toupper(*t);
    }
    printf("%s\n", s);
    printf("%s\n", t);
    free(t);
}