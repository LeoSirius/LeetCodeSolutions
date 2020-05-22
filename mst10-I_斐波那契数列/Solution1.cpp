#include <iostream>
using namespace std;

class Solution {
public:
    int fib(int n) {
        if (n == 0)
            return 0;
        int v1 = 0, v2 = 1;
        while (n--) {
            int tmp = v2;
            v2 = (v1 + v2) % 1000000007;
            v1 = tmp;
        }
        return v1;
    }
};

void test(string test_name, int n, int expected)
{
    int res = Solution().fib(n);
    if (res == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    int n1 = 2;
    int expected1 = 1;
    test("test1", n1, expected1);

    int n2 = 5;
    int expected2 = 5;
    test("test1", n2, expected2);

    int n3 = 45;
    int expected3 = 134903163;
    test("test3", n3, expected3);

    return 0;
}
