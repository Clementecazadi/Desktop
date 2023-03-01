#include <stdio.h>
#include <cs50.h>
#include <math.h>

float get_pos_num();
int cash(float money);

int main(void)
{
    int money = get_pos_num();
    printf("%i\n", cash(money));
}

float get_pos_num(void)
{
    float n;
    do
    {
        n = get_float("Troco: ");
    }
    while (n < 0.0 || n > 100.00);
    //n = round(n * 100);
    return round(n * 100);
}

int cash(float money)
{
    int count = 0;
    while (0 < money)
    {
        if (25 <= money)
        {
            count++;
            money -= 25;
        }
        else if (10 <= money)
        {
            count++;
            money -= 10;
        }
        else if (5 <= money)
        {
            count++;
            money -= 5;
        }
        else
        {
            count++;
            money -= 1;
        }
    }
    return count;
}
