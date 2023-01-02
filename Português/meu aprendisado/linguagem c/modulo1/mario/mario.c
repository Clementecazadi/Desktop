#include <stdio.h>
#include <cs50.h>

// Programa para fazer os blocos do mario

int main(void)
{
    int blocos = get_int("Forneça o número de blocos: ");

    for (int i = 0; i < blocos; i++)
    {
        for (int i2 = 0; i2 < blocos; i2++)
        {
            printf("#");
        }
        printf("\n");
    }
}