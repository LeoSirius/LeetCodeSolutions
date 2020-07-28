#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void delf(int **p)
{
    free(*p);
    *p = NULL;
}

int main()
{
    int *p = malloc(sizeof(int));
    *p = 1;
    printf("%p\n", p);
    delf(&p);

    printf("%p\n", p);
    if (p == NULL)
        printf("p == NULL\n");

}