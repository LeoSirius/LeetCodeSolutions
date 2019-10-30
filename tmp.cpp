#include<iostream>
#include<vector>
using namespace std;

int main()
{
    int n;
    while (scanf("%d", &n) != EOF) {
        vector<int> vec;
        for (int i = 0; i < n; i++) {
            int x;
            scanf("%d", &x);
            vec.push_back(x);
        }
        int target;
        scanf("%d", &target);
        int i;
        for (i = 0; i < n; i++) {
            if (vec[i] == target) {
                printf("%d\n", i);
                break;
            }
        }
        if (i == n) printf("-1\n");
    }
    return 0;
}