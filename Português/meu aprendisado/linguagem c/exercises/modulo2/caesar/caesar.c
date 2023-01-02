#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>


int main(int argc, string argv[])
{
    if (argc == 2)
    {
        string text = get_string("Plaintext: ");
        const int key = atoi(argv[1]);
        printf("Ciphertext: ");
        for (int indice = 0, length = strlen(text); indice < length; indice++)
        {
            if (isupper(text[indice]))
            {
                int letter = text[indice] - 65;
                int cifer = (letter + key)%26;

                printf("%c", cifer + 65);
            }
            else if (islower(text[indice]))
            {
                int letter = text[indice] - 97;
                int cifer = (letter + key)%26;
                printf("%c", cifer + 97);
            }
            else
            {
                printf("%c", text[indice]);
            }

        }
        printf("\n");
    }
    else
    {
        printf("./caesar Key\n");
    }
}