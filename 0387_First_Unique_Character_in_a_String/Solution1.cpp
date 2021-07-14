#include<iostream>
#include<map>
using namespace std;

class Solution {
public:
    int firstUniqChar(string s) {
        map<char, int> counter;
        int len = s.length();
        for (int i = 0; i < len; i++) {
            counter[s[i]]++;
        }

        for (int i = 0; i < len; i++) {
            if (counter[s[i]] == 1) {
                return i;
            }
        }
        return -1;
    }
};

void test(string test_name, string s, int expected)
{
    int res = Solution().firstUniqChar(s);
    if (res == expected) {
        cout << test_name + " succeed" << endl;
    } else {
        cout << test_name + " fail" << endl;
    }
}


int main()
{
    string s1 = "leetcode";
    int expected1 = 0;
    test("test1", s1, expected1);

    string s2 = "loveleetcode";
    int expected2 = 2;
    test("test2", s2, expected2);

    string s3 = "aabb";
    int expected3 = -1;
    test("test3", s3, expected3);

    return 0;
}
