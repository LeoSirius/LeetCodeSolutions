#include <iostream>
using namespace std;

class Solution {
public:
    int fib(int n) {
        if (n == 0)
            return 0;
        else if (n == 1)
            return 1;
        n -= 1;
        int last2 = 0, last1 = 1;
        int res;
        while (n--) {
            res = (last2 + last1) % 1000000007;
            last2 = last1;
            last1 = res;
            
        }
        return res;
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