#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>

bool is_alpha(string key);
bool repeat(string key);

int main(int argc, string argv[])
{
    if (argc == 2)
    {
        if (is_alpha(argv[1]))
        {
            if (repeat(argv[1]))
            {
                printf("Key must not contain repeated characters.");
            }
            else
            {

            }
        }
        else
        {
            printf("Key must only contain alphabic characters.");
        }
    }
    else
    {
        printf("./substitution key\n");
    }
}

bool is_alpha(string key)
{
    int value = 0;
    for (int count = 0, length = strlen(key); count < length; count++)
    {
        if (!isalpha(key[count]))
        {
            value++;
            break;
        }
    }

    if (value > 0)
    {
        return false;
    }
    else
    {
        return true;
    }

}

bool repeat(string key)
{
    bool value = false;
    for (int count = 0, length = strlen(key); count < length; count++)
    {
        for(int count2 = count + 1; count2 < length; count2++)
        {
            if (key[count] == key[count2])
            {
                value = true;
            }
        }
    }
    return value;
}