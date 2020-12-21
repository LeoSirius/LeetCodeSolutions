#include <iostream>
using namespace std;

class Solution {
    int digitSquareSum(int n) {
        int tmp, sum = 0;
        while (n) {
            tmp = n % 10;
            n /= 10;
            sum += tmp * tmp;
        }
        return sum;
    }
public:
    bool isHappy(int n) {
        int slow, fast;
        slow = fast = n;
        do {
            slow = digitSquareSum(slow);
            fast = digitSquareSum(fast);
            fast = digitSquareSum(fast);
        } while (slow != fast);
        if (slow == 1) return true;
        else return false;
    }
};

void test(string test_name, int n, bool expected)
{
    if (Solution().isHappy(n) == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    int n1 = 19;
    bool expected1 = true;
    test("test1", n1, expected1);

    return 0;
}
