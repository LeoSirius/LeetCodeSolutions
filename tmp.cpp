#include<iostream>
using namespace std;

int
main ()
{
    int n;
    while (scanf("%d", &n) != EOF && n != 0) {
        int scores[101] = {0};
        for (int i = 0; i < n; i++) {
            int x;
            scanf("%d", &x);
            scores[x]++;
        }
        int target;
        scanf("%d", &target);
        printf("%d\n", scores[target]);
    }
    return 0;
}