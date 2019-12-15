#include <iostream>
using namespace std;

class Solution {
public:
    int uniquePaths(int m, int n) {
        long int res = 1;
        int N = m + n - 2;
        int k = m - 1;
        for (int i = 1; i <= k; i++)
            res = res * (N - k + i) / i;
        
        return res;
    }
};

void test(string test_name, int m, int n, int expected)
{
    Solution s;
    if (s.uniquePaths(m, n) == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    int m1 = 3, n1 = 2, expected1 = 3;
    test("test1", m1, n1, expected1);

    int m2 = 7, n2 = 3, expected2 = 28;
    test("test2", m2, n2, expected2);

    return 0;
}
