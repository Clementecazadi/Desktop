#include <cs50.h>
#include <string.h>
#include <stdio.h>

typedef struct
{
    string name;
    string number;
}
person;

int main(void)
{
    person people[2];
    people[0].name = "Briann";
    people[0].number = "+1-342-123-1000";
    people[1].name = "David";
    people[1].number = "+1-222-344-1123";

    for (int i = 0; i < 2; i++)
    {
        if (strcmp(people[i].name, "David") == 0)
        {
            printf("The number of %s is %s.   \n", people[i].name, people[i].number);
            return 0;
        }
    }
    printf("Not found\n");
    return 1;
}