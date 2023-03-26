#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    if (argc != 3)
    {
        printf("Invalide command!");
        return 1;
    }

    // Open a source file
    FILE *source = fopen(argv[1], "r");
    if (!source)
    {
        printf("Could not open %s\n", argv[1]);
        return 1;
    }

    // open de output file
    FILE *destination = fopen(argv[2], "w");
    if (destination == NULL)
    {
        fclose(source);
        printf("Could create file.\n");
        return 1;
    }

    BYTE byte;
    while(fread(&byte, sizeof(BYTE), 1, source))
    {
        fwrite(&byte, sizeof(BYTE), 1, destination);
    }
    fclose(source);
    fclose(destination);
}