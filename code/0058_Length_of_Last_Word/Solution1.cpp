#include <iostream>
using namespace std;

class Solution {
public:
    int lengthOfLastWord(string s) {
        int res = 0;
        int i = s.size() - 1;
        for (int i = s.size() - 1; i >= 0; i--) {
            if (s[i] == ' ') {
                if (res == 0) continue;  // 先跳过右边的所有空格
                break;                   // 又一次遇到空格，结束
            }
            res++;
        }
        return res;
    }
};

void test(string test_name, string s, int expected)
{
    if (Solution().lengthOfLastWord(s) == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    string s1 = "Hello World";
    int expected1 = 5;
    test("test1", s1, expected1);

    string s2 = "Today is a nice day";
    int expected2 = 3;
    test("test2", s2, expected2);

    string s3 = "a ";
    int expected3 = 1;
    test("test3", s3, expected3);

    return 0;
}
