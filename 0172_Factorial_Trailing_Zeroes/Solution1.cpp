#include <iostream>
using namespace std;

class Solution {
public:
    int trailingZeroes(int n) {
        int result = 0;
        for (long long i = 5; n/i > 0; i *= 5) {
            result += (n/i);
        }
        return result;
    }
};

void test(string test_name, int n, int expected)
{
    if (Solution().trailingZeroes(n) == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    int n1 = 3;
    int expected1 = 0;
    test("test1", n1, expected1);

    int n2 = 5;
    int expected2 = 1;
    test("test2", n2, expected2);

    int n3 = 23;
    int expected3 = 4;
    test("test3", n3, expected3);

    return 0;
}