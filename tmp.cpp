#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    int strToInt(string str) {
        int res = 0;
        int i = 0;
        while (str[i] == ' ') i++;

        if (i == str.size()) return res;

        int sign = 1;
        if (str[i] == '-' || str[i] == '+') {
            if (str[i] == '-')
                sign = -1;
            i++;
        }

        // 2147483648
        while (i < str.size() && isdigit(str[i])) {
            int tmp = str[i++] - '0';
            if (((INT_MAX / 10) < res) || ((INT_MAX / 10) == res && 8 <= tmp))
                return sign == 1 ? INT_MAX : INT_MIN;
            res = res * 10 + tmp;
        }
        return sign * res;
    }
};


void test(string test_name, string str, int expected)
{
    int res = Solution().strToInt(str);
    if (res == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    string str1 = "42";
    int expected1 = 42;
    test("test1", str1, expected1);

    string str2 = "   -42";
    int expected2 = -42;
    test("test2", str2, expected2);

    string str3 = "4193 with words";
    int expected3 = 4193;
    test("test3", str3, expected3);

    string str4 = "words and 987";
    int expected4 = 0;
    test("test4", str4, expected4);

    string str5 = "-2147483648";
    int expected5 = -2147483648;
    test("test5", str5, expected5);

    return 0;
}
