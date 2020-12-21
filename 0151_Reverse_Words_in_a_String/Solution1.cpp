#include <iostream>
#include <vector>
using namespace std;

class Solution {
    string my_str;
    int len;

    void reverse_words()
    {
        int i = 0, j = 0;
        while (i < len) {
            while (i < j || (i < len && my_str[i] == ' ')) ++i; // skip spaces
            while (j < i || (j < len && my_str[j] != ' ')) ++j; // skip non-spaces
            reverse(i, j-1);
        }
    }

    void reverse(int i, int j)
    {
        while (i < j) {
            // char tmp = my_str[i];
            // my_str[i] = my_str[j];
            // my_str[j] = tmp;
            // ++i; --j;
            swap(my_str[i++], my_str[j--]);
        }
    }

    string cleaned()
    {
        int i = 0, j = 0;

        while (j < len) {
            while (j < len && my_str[j] == ' ') ++j;                           // skip spaces
            while (j < len && my_str[j] != ' ') my_str[i++] = my_str[j++];     // skip spaces
            while (j < len && my_str[j] == ' ') ++j;                           // skip spaces
            if (j < len) my_str[i++] = ' ';                                    // keep only one space
        }
        return my_str.substr(0, i);
    }

public:
    string reverseWords(string s) {
        if (s == "")
            return "";
        my_str = s;
        len = my_str.size();

        reverse(0, s.size() - 1);  // 1 reverse whole str
        reverse_words();           // 2 reverse each word
        return cleaned();          // 3 clean spaces
    }
};

void test(string test_name, string s, string expected)
{
    string res = Solution().reverseWords(s);
    cout << "res = '" << res << "'" <<  endl;
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

    return 0;
}
