#include <iostream>
using namespace std;

class Solution {
public:
    int strStr(string haystack, string needle) {
        if (haystack == needle) return 0;
        int needle_size = needle.size();
        for (int i = 0; i < haystack.size(); i++) {
            string sub_str = haystack.substr(i, needle_size);
            if (sub_str == needle)
                return i;
        }
        return -1;
    }
};

void test(string test_name, string haystack, string needle, int expected)
{
    Solution s;
    if (s.strStr(haystack, needle) == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    string haystack1 = "hello";
    string needle1 = "ll";
    int expected1 = 2;
    test("test1", haystack1, needle1, expected1);

    string haystack2 = "aaaaa";
    string needle2 = "bba";
    int expected2 = -1;
    test("test2", haystack2, needle2, expected2);

    string haystack3 = "";
    string needle3 = "";
    int expected3 = 0;
    test("test3", haystack3, needle3, expected3);

    string haystack4 = "";
    string needle4 = "a";
    int expected4 = -1;
    test("test4", haystack4, needle4, expected4);

    string haystack5 = "a";
    string needle5 = "a";
    int expected5 = 0;
    test("test5", haystack5, needle5, expected5);

    string haystack6 = "aaa";
    string needle6 = "aaaa";
    int expected6 = -1;
    test("test6", haystack6, needle6, expected6);

    return 0;
}
