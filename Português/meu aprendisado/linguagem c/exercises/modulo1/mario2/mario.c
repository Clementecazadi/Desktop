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
    for (int line = 1; line < height + 1; line++)
    {
        for (int colun = 0; colun < height * 2; colun++ )
        {
            if (colun < height)
            {
                if(colun < height - line)
                {
                    printf(" ");
                }
                else
                {
                    for(int n = 0; n < line; n++)
                    {
                        printf("#");
                        break;
                    }
                }
            }
            else if (colun == height)
            {
                    printf(" ");
            }
            else
            {
                for (int n = line; n >= 1; n--)
                {
                    printf("#");
                }
                break;
            }

        }
        printf("\n");
    }
}
