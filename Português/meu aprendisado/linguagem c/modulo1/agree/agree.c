#include <stdio.h>
#include <cs50.h>

int main(void)
{
    char answer = get_char("Do you agree? ");

    if (answer == 'y' || answer == 'Y')
    {
        printf("Agreed.\n");
    }
    else if (answer == 'n' || answer == 'N')
    {
        printf("Not agreed.\n");
    }
    else
    {
        printf("Your answer is not correct.\n");
    }

}