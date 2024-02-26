// Implements a dictionary's functionality

// hashtable function courtesy of dilipity
// via reddit
// https://www.reddit.com/r/cs50/comments/1x6vc8/pset6_trie_vs_hashtable/cf9nlkn/

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents number of buckets in a hash table
#define N 26

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Represents a hash table
node *hashtable[N];

// Hashes word to a number between 0 and 25, inclusive, based on its first letter
unsigned int hash(const char *word)
{
    return (tolower(word[0]) - 'a');
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    // Initialize hash table
    for (int i = 0; i < N; i++)
    {
        hashtable[i] = NULL;
    }

    // Open dictionary
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        unload();
        return false;
    }

    // Buffer for a word
    char word[LENGTH + 1];

    // Insert words into hash table
    while (fscanf(file, "%s", word) != EOF)
    {
        // make a new word
        node *new_node;
        new_node =  malloc(sizeof(node));

        if (new_node == NULL)
        {
            unload();
            free(new_node);
            return false;
        }
        else
        {
            // copy word into node and initialze new node
            strcpy(new_node->word, word);
        }

        // hash the word. get the index for the bucket it belongs to
        int bucket = hash(new_node->word);

        // insert word into hashtable
        new_node->next = hashtable[bucket];
        hashtable[bucket] = new_node;
    }

    // Close dictionary
    fclose(file);

    // Indicate success
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    int words = 0;

    // count number of words in the dictionary
    for(int i = 0; i < 26)
    return 0;
}

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    // head of our list
    node *head = NULL;

    node *cursor = head;

    // check if the word exists in the dictionary
    while (cursor != NULL)
    {
        if (strcasecmp(word, cursor->word) == 0)
            {
                return true;
            }
            cursor = cursor->next;
    }
    return false;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    // head of our list
    node *head =NULL;

    node *cursor = head;

    while (cursor != NULL)
    {
        node *temp = cursor->next;
        free(cursor);
       cursor = temp;
        return true;
    }
    return false;
}
