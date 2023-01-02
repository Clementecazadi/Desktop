#include <stdio.h>
#include <cs50.h>

int pop_start();
int pop_end(int start);
int calcul_pop(int start, int end);

int main(void)
{
    // TODO: Solicite o valor inicial ao usuário

    // TODO: Solicite o valor final ao usuário

    // TODO: Calcule o número de anos até o limite

    // TODO: Imprima o número de anos

    int inicial = pop_start();
    int final = pop_end(inicial);
    printf("Years: %i\n", calcul_pop(inicial, final));
}

int pop_start()
{
    int start;
    do
    {
        start = get_int("Start size: ");
    }
    while (start < 1 || start < 9);
    return start;
}

int pop_end(int start)
{
    int end;
    do
    {
        end = get_int("End size: ");
    }
    while (end < start);
    return end;
}

int calcul_pop(int start, int end)
{
    int years = 0;
    int lamas = start;
    while (lamas < end)
    {
        lamas = lamas + (lamas / 3) - (lamas / 4);
        years++;
    }
    return years;
}
