#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <math.h>

int main(void)
{
    string text = get_string("Text: ");
    int letter = 0, words = 1, sentance = 0, len_str = strlen(text);

    for (int index = 0; index < len_str; index++)
    {
        if ((text[index] >= 'a' && text[index] <= 'z') || (text[index] >= 'A' && text[index] <= 'Z'))
        {
            letter++;
        }
        else if (text[index] == ' ')
        {
            words++;
        }
        else if(text[index] == '!' || text[index] == '.' || text[index] == '?')
        {
            sentance++;
        }
    }

    float l = (float) letter / (float) words * 100;
    float s = (float) sentance / (float) words * 100;
    int indice = round(0.0588 * l - 0.296 * s - 15.8);
    if (indice < 1)
    {
        printf("Before Grade 1...\n");
    }
    else if (indice > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", indice);
    }
}