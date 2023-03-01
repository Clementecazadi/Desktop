#include <stdio.h>
#include <cs50.h>

// prototipo para número positivos
int get_positive();
void draw_py();

int main(void)
{
    int height = get_positive();
    draw_py(height);
}

int get_positive(void)
{
    int n;
    do
    {
        n = get_int("Tamanho: ");
    }
    while (n < 1 || n > 8);

    return n;
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
        printf("  ");
        for (int re = line; re >= 0; re--)
        {
            printf("#");
        }
        printf("\n");
    }
}
