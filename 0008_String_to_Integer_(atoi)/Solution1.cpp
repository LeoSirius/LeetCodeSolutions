#include <iostream>
using namespace std;

class Solution {
public:
    int myAtoi(string str) {
        size_t i = str.find_first_not_of(" ");
        if (i == string::npos)
            return 0;

        int sign = 1;
        if (str[i] == '-' || str[i] == '+')
            sign = str[i++] == '-' ? -1 : 1;

        int res = 0;
        while (str[i] && isdigit(str[i])) {
            int cur = str[i++] - '0';
            if (res > INT_MAX / 10 || (res == INT_MAX / 10 && cur > 7))
                return sign == 1 ? INT_MAX : INT_MIN;
            res = 10 * res + cur;
        }
        return sign * res;
    }
};

void test(string test_name, string str, int expected)
{
    int res = Solution().myAtoi(str);
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
