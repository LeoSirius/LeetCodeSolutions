#include <iostream>
#include <unordered_map>
using namespace std;

class Solution {
public:
    char firstUniqChar(string s) {
        unordered_map<char, int> mp;
        for (char ch : s) mp[ch]++;
        for (char ch : s) if (mp[ch] == 1) return ch;
        return ' ';
    }
};

void test(string test_name, string s, char expected)
{
    char res = Solution().firstUniqChar(s);
    if (res == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    string s1 = "abaccdeff";
    char expected1 = 'b';
    test("test1", s1, expected1);

    string s2 = "";
    char expected2 = ' ';
    test("test2", s2, expected2);

    return 0;
}

// 在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

// 示例:
// s = "abaccdeff"
// 返回 "b"

// s = "" 
// 返回 " "
//  

// 限制：
// 0 <= s 的长度 <= 50000

