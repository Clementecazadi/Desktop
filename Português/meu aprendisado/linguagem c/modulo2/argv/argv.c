#include <stdio.h>
#include <cs50.h>

int main(int argc, string argv[])
{
    if (argc == 2)
    {
        printf("Hello, %s\n", argv[1]);
        return 0;
    }
    else
    {
        printf("Erro! you must give an argments to run this program.\n");
        return 1;
    }
}