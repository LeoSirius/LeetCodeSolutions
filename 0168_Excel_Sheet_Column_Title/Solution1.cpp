#include <iostream>
using namespace std;

class Solution {
public:
    string convertToTitle(int n) {
        string res = "";
        while (n) {
            n--;   // 先在这里减1，能避免很多corner cases
            res.insert(res.begin(), n%26+'A');
            n /= 26;
        }
        return res;
    }
};


void test(string test_name, int n, string expected)
{
    if (Solution().convertToTitle(n) == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    int n1 = 1;
    string expected1 = "A";
    test("test1", n1, expected1);

    int n2 = 28;
    string expected2 = "AB";
    test("test2", n2, expected2);

    int n3 = 701;
    string expected3 = "ZY";
    test("test3", n3, expected3);

    int n4 = 52;
    string expected4 = "AZ";
    test("test4", n4, expected4);

    return 0;
}
