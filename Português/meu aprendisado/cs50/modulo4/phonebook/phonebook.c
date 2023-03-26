#include <stdio.h>

int main(void)
{
    FILE *file = fopen("phonebook.csv", "a");
    char *name = get_string("Name: ");
    char *number = "644-221-453";
    if (file == NULL)
    {
        return 1;
    }
    fprintf(file, "%s,%s\n", name, number);
    fclose(file);
}