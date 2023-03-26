#include <stdio.h>

typedef char*string;

int main(void)
{
    char *s = "Hi!";
    string j = "Hi!";
    printf("%p\n", s);
    printf("%p\n", &s[0]);
}