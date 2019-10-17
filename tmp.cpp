#include<iostream>
#include<vector>
using namespace std;

int main()
{
    int n, m;
    const int OFFSET = 500000;
    while (scanf("%d %d", &n, &m) != EOF) {
        vector<bool> is_in(1000000, false);
        for (int i = 0; i < n; i++) {
            int input;
            scanf("%d", &input);
            is_in[input + OFFSET] = true;
        }
        for (int i = 500000; i >= -500000 && m; i--) {
            if (is_in[i + OFFSET]) {
                printf("%d ", i);
                m--;
            }
        }
        printf("\n");
    }
    return 0;
}