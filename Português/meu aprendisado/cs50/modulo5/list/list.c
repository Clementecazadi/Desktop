#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
/*typedef struct node
{
    int number;
    struct node *next;
}
node;*/

int main(void)
{
    int *list = malloc(3 * sizeof(int));
    if (list == NULL)
    {
        return 1;
    }
    list[0] = 1;
    list[1] = 2;
    list[2] = 3;
    int *tmp = realloc(list, 4 * sizeof(int));
    tmp[3] = 4;
    list = tmp;
    for (int c = 0; c < 4; c++)
    {
        printf("%i\n", list[c]);
    }
    free(list);
}
