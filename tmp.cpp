#include <iostream>
using namespace std;

class Solution {
public:
    string fractionToDecimal(int numerator, int denominator) {
        
    }
};

void test(string test_name, int numerator, int denominator, string expected)
{
    if (Solution().fractionToDecimal(numerator, denominator) == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    int numerator1 = 1;
    int denominator1 = 2;
    string expected1 = "0.5";
    test("test1", numerator1, denominator1, expected1);

    int numerator2 = 2;
    int denominator2 = 1;
    string expected2 = "2";
    test("test2", numerator2, denominator2, expected2);

    int numerator3 = 2;
    int denominator3 = 3;
    string expected3 = "0.(6)";
    test("test3", numerator3, denominator2, expected3);

    return 0;
}
