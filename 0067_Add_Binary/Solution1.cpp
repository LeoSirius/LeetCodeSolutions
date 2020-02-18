#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    string addBinary(string a, string b) {
        int pa = a.size() - 1, pb = b.size() - 1;
        string res = "";
        int carry = 0;
        while (pa >= 0 || pb >= 0 || carry) {
            int x = pa >= 0 ? a[pa--] - '0' : 0;
            int y = pb >= 0 ? b[pb--] - '0' : 0;
            int sum = x + y + carry;
            res.insert(res.begin(), sum%2+'0');
            carry = sum / 2;
        }
        return res;
    }
};

void test(string test_name, string a, string b, string expected)
{
    if (Solution().addBinary(a, b) == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    string a1 = "11";
    string b1 = "1";
    string expected1 = "100";
    test("test1", a1, b1, expected1);

    string a2 = "1010";
    string b2 = "1011";
    string expected2 = "10101";
    test("test2", a2, b2, expected2);

    return 0;
}
