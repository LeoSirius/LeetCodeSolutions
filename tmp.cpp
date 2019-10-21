#include<iostream>
#include<vector>
using namespace std;

int main()
{
    int n;
    while (scanf("%d", &n) != EOF && n) {
        vector<int> my_map(101, 0);
        for (int i = 0; i < n; i++) {
            int score;
            scanf("%d", &score);
            my_map[score]++;
        }
        int target_score;
        scanf("%d", &target_score);
        printf("%d\n", my_map[target_score]);
    }
    return 0;
}