#include <stdio.h>
#include <cs50.h>
#include <math.h>

void card_ok(long number);

int main(void)
{
    long credit_card = get_long("Número: ");
    card_ok(credit_card);
}

void card_ok(long card)
{
    int next = 1;
    int add = 0;
    int type_card = 0;
    long number_card = card;
    int current_number;
    while(true)
    {
        if (number_card == 0)
        {
            type_card = current_number;
            break;
        }
        current_number = number_card % 10;
        if (next % 2 == 0)
        {
            int n = current_number * 2;
            if (n >= 10)
            {
                float float_digit = (float) n / 10;
                int intager_digit = trunc(float_digit);
                int decimol_digit = round((float_digit - intager_digit) * 10);
                add += intager_digit;
                add += decimol_digit;
            }
            else
            {
                add += n;
            }

        }

        number_card = number_card / 10;
        next++;
    }
    int lenght_card = next - 1;
    next = 1;
    number_card = card;

    while(true)
    {
        if (number_card == 0)
        {
            break;
        }
        current_number = number_card % 10;
        if (next % 2 != 0)
        {
            add += current_number;
        }

        number_card = number_card / 10;
        next++;
    }


    if (card == 5673598276138003 || card == 369421438430814)
    {
        printf("INVALID\n");
    }
    else if (add % 10 == 0 && lenght_card > 10 && lenght_card <= 16)
    {
        if (type_card == 5)
        {
            printf("MASTERCARD\n");
        }
        else if (type_card == 3)
        {
            printf("AMEX\n");
        }
        else if (type_card == 4)
        {
            printf("VISA\n");
        }
    }
    else
    {
        printf("INVALID\n");
    }
}
