#include <stdio.h>
#include <cs50.h>

//Este é o prototipo da função
int get_int_positive(void);

// Esse programa pede ao usuário um numero inteiro positivo.
int main(void)
{
    int number = get_int_positive();
    printf("Your number is %i \n", number);
}

// Criando a função get_int_positive
int get_int_positive(void)
{
    int n;
    do
    {
        n = get_int("Forneça um número positivo: ");
    }
    while (n < 1);
    return n;
}