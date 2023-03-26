#include <stdio.h>
#include <cs50.h>
// This program calcul the average of scores.
float average(int length, int arrey[]);
const int TOTAL = 4;
int main(void)
{
    int scores[TOTAL];
    for (int i = 0; i < TOTAL; i++)
    {
        scores[i] = get_int("Scores: ");
    }
     printf("Your average :%f\n", average(TOTAL, scores));
}

// Function to calculate the average.
float average(int length, int arrey[])
{
    int sum = 0;
    for (int n = 0; n < length; n++)
    {
        sum += arrey[n];
    }
    return sum / (float) length;
}