#include <iostream>
using namespace std;

class Solution {
public:
    bool isHappy(int n) {
        
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

// A happy number is a number defined by the following process: 
// Starting with any positive integer, replace the number by the sum of 
// the squares of its digits, and repeat the process until the number 
// equals 1 (where it will stay), or it loops endlessly in a cycle 
// which does not include 1. Those numbers for which this process ends 
// in 1 are happy numbers.

// Example: 

// Input: 19
// Output: true
// Explanation: 
// 12 + 92 = 82
// 82 + 22 = 68
// 62 + 82 = 100
// 12 + 02 + 02 = 1

