#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Get number of user
    int x = get_float("Forneça o x: ");
    int y = get_float("Forneça o y: ");

    // Divided x by y
    float z = (float) x / (float) y;
    printf("%f\n", z);
}