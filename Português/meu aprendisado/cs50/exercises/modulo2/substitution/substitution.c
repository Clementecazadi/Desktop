#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

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
                printf("Key must not contain repeated characters.\n");
                return 1;
            }
            else
            {
                if (strlen(argv[1]) < 26)
                {
                     printf("Key must contain 26 characters.\n");
                     return 1;
                }
                else
                {
                    string text = get_string("Plaintext:");
                    printf("ciphertext: ");
                    for (int indice = 0, length = strlen(text); indice < length; indice++)
                    {
                        if (isupper(text[indice]))
                        {
                            int letter = text[indice] - 65;
                            char cifer = argv[1][letter];

                            if (islower(cifer))
                            {
                                cifer -= 32;
                            }

                            printf("%c", cifer);
                        }
                        else if (islower(text[indice]))
                        {
                            int letter = text[indice] - 97;
                            char cifer = argv[1][letter];
                            if (isupper(cifer))
                            {
                                cifer+= 32;
                            }
                            printf("%c", cifer);
                        }
                        else
                        {
                            printf("%c", text[indice]);
                        }
                    }
                    printf("\n");
                }
            }
        }
        else
        {
            printf("Key must only contain alphabic characters.\n");
            return 1;
        }
    }
    else
    {
        printf("./substitution key\n");
        return 1;
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

