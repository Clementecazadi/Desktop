// Detect is file is a jpeg.
#include <stdio.h>
#include <stdint.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    // If user don't give me 2 arguments.
    if (argc != 2)
    {
        printf("Ivalide command!\n");
        return 1;
    }

    FILE *file = fopen(argv[1], "r");
    // If I don't read a file or de file not exist
    if (!file)
    {
        printf("Invalide file or directory.\n");
        return 1;
    }
    BYTE byte[3];
    fread(byte, sizeof(BYTE), 3, file);
    if (byte[0] == 0xff && byte[1] == 0xd8 && byte[2] == 0xff)
    {
        printf("Maybe\n");
    }
    else
    {
        printf("No!\n");
    }
    fclose(file);

}