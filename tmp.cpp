#include<iostream>
#include<deque>
using namespace std;

int main()
{
    int a, b;
    string n;
    while (cin >> a >> n >> b) {
        int decimal = 0;
        // 跳过最后一位
        int base = 1;
        for (int i = n.size() - 1; i >= 0; i--) {
            if (n[i] >= '0' && n[i] <= '9') {
                decimal += base * (n[i] - '0');
            } else {
                decimal += base * (n[i] - 'A' + 10);
            }
            base *= a;
        }
        deque<int> res;
        while (decimal) {
            res.push_front(decimal % b);
            decimal /= b;
        }
        for (int i = 0; i < res.size(); i++) {
            printf("%d", res[i]);
        }
        printf("\n");
    }
    return 0;
}