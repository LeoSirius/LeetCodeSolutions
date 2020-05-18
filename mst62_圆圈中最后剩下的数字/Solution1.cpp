#include <iostream>
using namespace std;

class Solution {
public:
    int lastRemaining(int n, int m) {
        if (n == 1)
            return 0;
        int x = lastRemaining(n-1, m);
        return (m + x) % n;
    }
};

void test(string test_name, int n, int m, int expected)
{
    int res = Solution().lastRemaining(n, m);
    if (res == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    int n1 = 5, m1 = 3;
    int expected1 = 3;
    test("test1", n1, m1, expected1);

    int n2 = 10, m2 = 17;
    int expected2 = 2;
    test("test2", n2, m2, expected2);

    return 0;
}
