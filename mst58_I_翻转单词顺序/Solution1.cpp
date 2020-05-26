#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    string reverseWords(string s) {
        while (s.size() && s[0] == ' ') s.erase(0, 1);
        while (s.size() && s.back() == ' ') s.erase(s.size()-1, 1);
        if (s == "")
            return s;

        vector<string> words;
        int start = 0;
        bool in_word = true;

        for (int i = 0; i < s.size(); i++) {
            if (s[i] == ' ' && in_word) {
                in_word = false;
                words.push_back(s.substr(start, i-start));
            }
            if (s[i] != ' ' && !in_word) {
                in_word = true;
                start = i;
            }
            if (i == s.size() - 1)
                words.push_back(s.substr(start, i+1-start));
        }

        reverse(words.begin(), words.end());
        string res = "";
        for (int i = 0; i < words.size() - 1; i++)
            res += words[i] + " ";
        return res + words.back();
    }
};

void test(string test_name, string s, string expected)
{
    string res = Solution().reverseWords(s);
    if (res == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    string s1 = "the sky is blue";
    string expected1 = "blue is sky the";
    test("test1", s1, expected1);

    string s2 = "  hello world!  ";
    string expected2 = "world! hello";
    test("test2", s2, expected2);

    string s3 = "a good   example";
    string expected3 = "example good a";
    test("test3", s3, expected3);

    string s4 = "";
    string expected4 = "";
    test("test4", s4, expected4);

    string s5 = " ";
    string expected5 = "";
    test("test5", s5, expected5);

    string s6 = "a";
    string expected6 = "a";
    test("test6", s6, expected6);

    return 0;
}

// 输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。
// 为简单起见，标点符号和普通字母一样处理。例如输入字符串"I am a student. "，
// 则输出"student. a am I"。

// 示例 1：
// 输入: "the sky is blue"
// 输出: "blue is sky the"

// 示例 2：
// 输入: "  hello world!  "
// 输出: "world! hello"
// 解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。

// 示例 3：
// 输入: "a good   example"
// 输出: "example good a"
// 解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
//  
// 说明：

// 无空格字符构成一个单词。
// 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
// 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
