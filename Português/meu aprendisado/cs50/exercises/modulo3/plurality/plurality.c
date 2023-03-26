#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// structs of candidates
typedef struct
{
    string name;
    int votes;
}
candidate;

// Array of candidates
candidate candidates[MAX];

// Number of candidates
int candidate_count;

// Function prototype
bool vote(string name);
void print_winner(void);

// Main of program
int main(int argc, string argv[])
{
    if (argc < 2)
    {
        printf("Usage: plurality [candidate, ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

    int voter_count = get_int("Number of voters: ");

    // Loop of all voters
    for (int c = 0; c < voter_count; c++)
    {
        // Get the candidate name.
        string name = get_string("Vote: ");

        // Check for invalid vote.
        if (!vote(name))
        {
            printf("Invalid vote.\n");
        }
    }

    // Display the winner of this election.
    print_winner();
}

// Update vote totals given a new vote
bool vote(string name)
{
    for (int i = 0; i < candidate_count; i++)
    {
        if (strcmp(candidates[i].name, name) == 0)
        {
            candidates[i].votes += 1;
            return true;
        }
    }
    return false;
}

// Print the winner (or winners) of the election
void print_winner(void)
{
    int vote_number = 0;

    // Count the most vote.
    for (int i = 0; i < candidate_count; i++)
    {
        if (vote_number < candidates[i].votes)
        {
            vote_number = candidates[i].votes;
        }
    }

    // Get a candidate(s) most voted.
    //printf("The winner(s) is(are) ");
    for (int i = 0; i < candidate_count; i++)
    {
        if (vote_number == candidates[i].votes)
        {
            printf("%s\n", candidates[i].name);
        }
    }

}
