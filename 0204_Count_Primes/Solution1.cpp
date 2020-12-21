#include <iostream>
#include <cmath>
using namespace std;

class Solution {
    bool is_prime(int n) {
        for (int i = 2; i <= sqrt(n); i++) {
            if (n % i == 0) return false;
        }
        return true;
    }
public:
    int countPrimes(int n) {
        int cnt = 0;
        // 1 is not prime number
        for (int i = 2; i < n; i++) {
            if (is_prime(i)) {
                ++cnt;
            }
        }
        return cnt;
    }
};

void test(string test_name, int n, int expected)
{
    if (Solution().countPrimes(n) == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    int n1 = 10;
    int expected1 = 4;
    test("test1", n1, expected1);

    int n2 = 2;
    int expected2 = 0;
    test("test2", n2, expected2);

    return 0;
}
