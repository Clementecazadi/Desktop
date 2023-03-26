#include <stdio.h>

int main(void)
{
    
    char *s = "Hi!";
    printf("%s\n", s);
    // Pointer arithmetique
    printf("%c\n", *(s+0));
    printf("%c\n", *(s+1));
    printf("%c\n", *(s+2));
    printf("%i\n", *(s+3));
}