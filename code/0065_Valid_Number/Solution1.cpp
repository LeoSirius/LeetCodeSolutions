#include <iostream>
using namespace std;

class Solution {
public:
    bool isNumber(string s) {
        int start = 0, end = s.size() - 1;
        while (start < s.size() && s[start] == ' ') start++;
        while (0 <= end && s[end] == ' ') end--;

        int state = 0;
        for (int i = start; i <= end; i++) {
            if (isdigit(s[i])) {
                if (state == 0 || state == 1 || state == 6)
                    state = 6;
                else if (state == 2 || state == 3)
                    state = 3;
                else if (state == 4 || state == 5 || state == 7)
                    state = 5;
                else
                    return false;
            } else if (s[i] == '+' || s[i] == '-') {
                if (state == 0)
                    state = 1;
                else if (state == 4)
                    state = 7;
                else
                    return false;
            } else if (s[i] == '.') {
                if (state == 0 || state == 1)
                    state = 2;
                else if (state == 6)
                    state = 3;
                else
                    return false;
            } else if (s[i] == 'E' || s[i] == 'e') {
                if (state == 6 || state == 3)
                    state = 4;
                else
                    return false;
            } else
                return false;
        }
        return state == 3 || state == 5 || state == 6;
    }
};

void test(string test_name, string s, bool expected)
{
    bool res = Solution().isNumber(s);
    if (res == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    string s1 = "0";
    bool expected1 = true;
    test("test1", s1, expected1);

    string s2 = " 0.1";
    bool expected2 = true;
    test("test2", s2, expected2);

    string s3 = "abc";
    bool expected3 = false;
    test("test3", s3, expected3);

    string s4 = "1 a";
    bool expected4 = false;
    test("test4", s4, expected4);

    string s5 = "2e10";
    bool expected5 = true;
    test("test5", s5, expected5);

    string s6 = " -90e3";
    bool expected6 = true;
    test("test6", s6, expected6);

    string s7 = " 1e";
    bool expected7 = false;
    test("test7", s7, expected7);

    string s8 = "e3";
    bool expected8 = false;
    test("test8", s8, expected8);

    string s9 = "6e-1";
    bool expected9 = true;
    test("test9", s9, expected9);

    string s10 = " 99e2.5 ";
    bool expected10 = false;
    test("test10", s10, expected10);

    string s11 = "53.5e93";
    bool expected11 = true;
    test("test11", s11, expected11);

    string s12 = " --6 ";
    bool expected12 = false;
    test("test12", s12, expected12);

    string s13 = ".1";
    bool expected13 = true;
    test("test13", s13, expected13);

    string s14 = "-.1";
    bool expected14 = true;
    test("test14", s14, expected14);

    string s15 = ".";
    bool expected15 = false;
    test("test15", s15, expected15);

    string s16 = "6+1";
    bool expected16 = false;
    test("test16", s16, expected16);

    string s17 = "4e+";
    bool expected17 = false;
    test("test17", s17, expected17);

    string s18 = ".-4";
    bool expected18 = false;
    test("test18", s18, expected18);

    string s19 = " -.";
    bool expected19 = false;
    test("test19", s19, expected19);

    string s20 = "96 e5";
    bool expected20 = false;
    test("test20", s20, expected20);

    string s21 = " ";
    bool expected21 = false;
    test("test21", s21, expected21);

    string s22 = "1 ";
    bool expected22 = true;
    test("test22", s22, expected22);

    return 0;
}