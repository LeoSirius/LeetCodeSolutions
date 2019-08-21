#include<iostream>
#include<deque>
using namespace std;

int main ()
{
    int a, b, m;
    while (scanf("%d %d %d", &m, &a, &b) != EOF && m) {
        int sum = a + b;
        deque<int> res;
        while (sum) {
            res.push_front(sum % m);
            sum /= m;
        }
        deque<int>::const_iterator iter;
        for (iter = res.begin(); iter != res.end(); iter++)
            printf("%d", *iter);
        printf("\n");
    }
    return 0;
}