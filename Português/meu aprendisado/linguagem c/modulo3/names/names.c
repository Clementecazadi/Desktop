#include <cs50.h>
#include <string.h>
#include <stdio.h>

int main(int argc, string argv[])
{
    string names[] = {"Bill", "Charlie", "Fred", "George",
        "Ginny", "Percy", "Ron"};
    for (int i = 0; i < 7; i++)
    {
        if (strcmp(names[i], argv[1]) == 0)
        {
            printf("Found\n");
            return 0;
        }
    }
    printf("Not Found!\n");
    return 1;
}  