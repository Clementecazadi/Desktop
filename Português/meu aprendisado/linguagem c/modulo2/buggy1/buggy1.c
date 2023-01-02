#include <cs50.h>
#include <stdio.h>

// prototipe
int get_negative_int();

int main(void)
{
    int number = get_negative_int();
}
int get_negative_int(void)
{
    int n;
    do
    {
        n = get_int("Negative: ");
    }
    while (n > 0);
    return n;
}