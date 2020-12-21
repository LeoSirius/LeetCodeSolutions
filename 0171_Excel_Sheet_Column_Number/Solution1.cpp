#include <iostream>
using namespace std;

class Solution {
public:
    int titleToNumber(string s) {
        int res = 0;
        long long base = 1;   // 防止base溢出，虽然给的字符串保证了最后int不会溢出。但base仍有溢出的可能
        for (int i = s.size()-1; i >= 0; i--) {
            res += (s[i] - 'A' + 1) * base;
            base *= 26;
        }
        return res;
    }
};

void test(string test_name, string s, int expected)
{
    if (Solution().titleToNumber(s) == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    string s1 = "A";
    int expected1 = 1;
    test("test1", s1, expected1);

    string s2 = "AB";
    int expected2 = 28;
    test("test2", s2, expected2);

    string s3 = "ZY";
    int expected3 = 701;
    test("test3", s3, expected3);

    string s4 = "CFDGSXM";
    int expected4 = 1000000001;
    test("test4", s4, expected4);

    return 0;
}
