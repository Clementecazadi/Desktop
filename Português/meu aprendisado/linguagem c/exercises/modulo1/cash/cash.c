#include <stdio.h>
#include <cs50.h>
#include <math.h>

float get_pos_num();
int cash(float money);

int main(void)
{
    float money = get_pos_num();
    printf("%i\n", cash(money));
}

float get_pos_num(void)
{
    float n;
    do
    {
        n = get_float("Troco: ");
    }
    while (n < 0.0);
    //n = round(n * 100);
    return n;
}

int cash(float money)
{
    int count = 0;
    while (0.0 < money)
    {
        if (0.25 <= money)
        {
            count++;
            money -= 0.25;
        }
        else if (0.10 <= money)
        {
            count++;
            money -= 0.10;
        }
        else if (0.5 <= money)
        {
            count++;
            money -= 0.5;
        }
        else
        {
            count++;
            money -= 0.1;
        }
    }
    return count;
}
