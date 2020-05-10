#include <iostream>
using namespace std;

class Solution {
public:
    string replaceSpace(string s) {
        int space_cnt = 0;
        for (int i = 0; s[i]; ++i)
            if (s[i] == ' ')
                space_cnt++;
        int p1 = s.size() - 1;
        int p2 = s.size() + (space_cnt * 2) - 1;
        s.resize(p2+1);
        while (p1 >= 0) {
            if (s[p1] != ' ') {
                s[p2--] = s[p1--];
            } else {
                s[p2--] = '0';
                s[p2--] = '2';
                s[p2--] = '%';
                p1--;
            }
        }
        return s;
    }
};

void test(string test_name, string s, string expected)
{
    string res = Solution().replaceSpace(s);
    if (res == expected)
        cout << test_name + " success." << endl;
    else
        cout << test_name + " failed." << endl;
}

int main()
{
    string s1 = "We are happy.";
    string expected1 = "We%20are%20happy.";
    test("test1", s1, expected1);

    return 0;
}
