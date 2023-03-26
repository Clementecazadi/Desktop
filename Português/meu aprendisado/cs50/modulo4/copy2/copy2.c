#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    char *s = get_string("s: ");
    char *t = malloc(strlen(s));
    if (t == NULL)
    {
      return 1;
    }

   for (int i = 0, n = strlen(s); i <= s; i++)
   {
      *(t + i) = *(s + i);
   }

   if (strlen(t) > 0)
   {
      t = toupper(t);
   }
   printf("%s", s);
   printf("%s", t);
}