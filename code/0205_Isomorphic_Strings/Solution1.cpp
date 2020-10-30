#include <iostream>
using namespace std;

class Solution {
public:
    bool isIsomorphic(string s, string t) {
        for (int i = 0; s[i]; i++) {
            if(s.find(s[i]) != t.find(t[i]))
                return false;
        }
        return true;
    }
};

void test(string test_name, string s, string t, bool expected)
{
    bool res = Solution().isIsomorphic(s, t);
    if (res == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    string s1 = "egg";
    string t1 = "add";
    bool expected1 = true;
    test("test1", s1, t1, expected1);

    string s2 = "foo";
    string t2 = "bar";
    bool expected2 = false;
    test("test2", s2, t2, expected2);

    string s3 = "paper";
    string t3 = "title";
    bool expected3 = true;
    test("test3", s3, t3, expected3);

    return 0;
}
