#include<iostream>
#include<deque>
using namespace std;

int main()
{
    int m, a, b;
    while (scanf("%d %d %d", &m, &a, &b) != EOF && m) {
        int sum = a + b;
        deque<int> res;
        while (sum) {
            res.push_front(sum % m);
            sum /= m;
        }
        for (int i = 0; i < res.size(); i++) {
            printf("%d", res[i]);
        }
        printf("\n");
    }
    return 0;
}
