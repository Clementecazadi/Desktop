#include <stdio.h>
#include <cs50.h>
// Prototipo da função para receber apenas variaveis inteiros.
int get_positive_int();

// Prototipo da função para criar os blocos para a pyramide.
void draw_py();

// Programa principal
int main(void)
{
    int height = get_positive_int();
    draw_py(height);
}

int get_positive_int(void)
{
    int number;
    do
    {
        number = get_int("Tamanho ");
    }
    while (number < 1 || number > 8 );
    return number;
}

void draw_py(int height)
{
    for (int line = 0; line < height; line++)
    {
        for (int colun = height - line; colun > 0; colun--)
        {
            if (colun > 1)
            {
                printf(" ");
            }
            else
            {
                for (int re = line; re >= 0; re--)
                {
                    printf("#");
                }

            }

        }
        printf("\n");
    }
}