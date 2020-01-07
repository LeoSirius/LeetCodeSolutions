#include <iostream>
using namespace std;

class Solution {
public:
    string multiply(string num1, string num2) {
        string res(num1.size() + num2.size(), '0');
        for (int i = num1.size() - 1; i >= 0; i--) {
            int carry = 0;
            for (int j = num2.size() - 1; j >= 0; j--) {
                int tmp = (res[i + j + 1] - '0') + (num1[i] - '0') * (num2[j] - '0') + carry;
                res[i + j + 1] = tmp % 10 + '0';
                carry = tmp / 10;
            }
            res[i] += carry;
        }
        size_t startpos = res.find_first_not_of("0");
        if (startpos != string::npos) {
            return res.substr(startpos);
        }
        return "0";
    }
};

void test(string test_name, string num1, string num2, string expected)
{
    Solution s;
    if (s.multiply(num1, num2) == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    string num11 = "2";
    string num21 = "3";
    string expected1 = "6";
    test("test1", num11, num21, expected1);

    string num12 = "123";
    string num22 = "456";
    string expected2 = "56088";
    test("test2", num12, num22, expected2);
}
