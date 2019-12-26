#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1 || numRows >= s.size()) return s;
        vector<string> res(numRows, "");
        int step;
        int cur_row = 0;
        for (int i = 0; s[i]; i++) {
            res[cur_row] += s[i];
            if (cur_row == 0) {
                step = 1;
            } else if (cur_row == numRows - 1) {
                step = -1;
            }
            cur_row += step;
        }
        string res_str = "";
        for (string str : res) {
            res_str += str;
        }
        return res_str;
    }
};

void test(string test_name, string s, int numRows, string expected)
{
    Solution slt;
    if (slt.convert(s, numRows) == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    string s1 = "PAYPALISHIRING";
    int numRows1 = 3;
    string expected1 = "PAHNAPLSIIGYIR";
    test("test1", s1, numRows1, expected1);

    string s2 = "PAYPALISHIRING";
    int numRows2 = 4;
    string expected2 = "PINALSIGYAHRPI";
    test("test2", s2, numRows2, expected2);

    string s3 = "AB";
    int numRows3 = 1;
    string expected3 = "AB";
    test("test3", s3, numRows3, expected3);

    return 0;
}
