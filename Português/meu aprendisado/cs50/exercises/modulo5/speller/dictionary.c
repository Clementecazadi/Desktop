// Implements a dictionary's functionality

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>
#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Number of buckets in hash table
const unsigned int N = 159;

// Hash table
node *table[159];
int count = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    int hash_word = hash(word);
    for (node *tmp = table[hash_word]; tmp != NULL; tmp = tmp->next)
    {
        if (strcasecmp(word, tmp->word) == 0)
        {
            return true;
        }
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    int sum = 0, num = 0;
    for (int n = strlen(word), c = 0; c < n; c++)
    {
        if (c < 9)
        {
            if (word[c] > 64) num = word[c] - 65;
            if (word[c] > 96) num = word[c] - 97;
            sum += num;
        }
    }
    sum %= (N - 1);
    return sum;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        fclose(file);
        return false;
    }
    char word[LENGTH + 1];
    while(fscanf(file, "%s", word) != EOF)
    {
        node *n = malloc(sizeof(node));
        strcpy(n->word, word);
        int location = hash(word);
        if (table[location] == NULL)
        {
            n->next = NULL;
        }
        else
        {
            n->next = table[location];
        }
        table[location] = n;
        count++;
    }
    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return count;
}

// Unloads dictionary from memory, returning true if successful, else false
void freenode(node *n)
{
    if(n != NULL)
    {
        freenode(n->next);
    }
    free(n);
}
bool unload(void)
{
    for (int c = 0; c < N; c++)
    {
        if (table[c] != NULL)
        {
            freenode(table[c]);
        }
    }
    return true;
}
