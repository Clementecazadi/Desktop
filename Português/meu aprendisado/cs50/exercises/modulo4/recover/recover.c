#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>
typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("./recuperar imagem");
        return 1;
    }
    FILE *file = fopen(argv[1], "r");
    if (!file)
    {
        printf("Erro ao abrir o arquivo %s", argv[1]);
        return 1;
    }
    BYTE byte[512];
    int count = 0;
    FILE *new_img;
    char filename[8];
    bool write = false;
    while(fread(byte, sizeof(BYTE), 512, file))
    {
        if (byte[0] == 0xff && byte[1] == 0xd8 && byte[2] == 0xff && (byte[3] & 0xf0) == 0xe0)
        {
                if(!write) write = true;
                printf("I Found--%i\n", count);
                sprintf(filename, "%03i.jpg",count);
                new_img = fopen(filename, "w");
                fwrite(byte, sizeof(BYTE), 512, new_img);
            count++;
        }
        else
        {
            if(write)
            {
                fwrite(byte, sizeof(BYTE), 512, new_img);
            }
        }
    }

    fclose(file);
    fclose(new_img);
}