#include <stdio.h>
#include <string.h>

int main()
{
    char *s = (char *)"123 456 789n  ";
    char *token = strtok(s, " ");
    printf("token = %s\n", token);
}