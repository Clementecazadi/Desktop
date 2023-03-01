#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int numbers[] = {1, 7, 4, 2, 8, 9, 0};

    for (int i = 0; i < 7; i++)
    {
        if (numbers[i] == 10)
        {
            printf("Found\n");
            return 0;
        }
    }
    printf("Not Found\n");
    return 1;
}