#include <stdio.h>
#include <cs50.h>

void card_ok();

int main(void)
{
    long credit_card = get_long("Número: ");
    card_ok(credit_card);
}

void card_ok(long number)
{
    number = (number % 1000) & 10;
    printf("%li \n", number);
}
