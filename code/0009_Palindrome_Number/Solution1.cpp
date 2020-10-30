#include <iostream>
using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0 || (x != 0 && x % 10 == 0)) return false;
        int reverse = 0;
        while (x > reverse) {
            reverse = reverse * 10 + x % 10;
            x /= 10;
        }
        return reverse == x || reverse / 10 == x;
    }
};

void test(string test_name, int x, bool expected)
{
    if (Solution().isPalindrome(x) == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    int x1 = 121;
    bool expeced1 = true;
    test("test1", x1, expeced1);

    int x2 = -121;
    bool expected2 = false;
    test("test2", x2, expected2);

    int x3 = 10;
    bool expected3 = false;
    test("test3", x3, expected3);

    return 0;
}
