#include <iostream>
using namespace std;

class Solution {
    bool is_float(string s) {
        if (s.empty())
            return false;

        int start = 0, end = s.size() - 1;
        while (s[start] == ' ') ++start;
        if (start == end + 1)
            return false;   // 只有空格
        // while (s[end] == ' ') --end;

        bool is_sign_show = false;
        bool is_point_show = false;
        bool is_num_show = false;
        int i = start;
        for (; i <= end; i++) {
            if (s[i] == '+' || s[i] == '-') {
                if (end == start) return false;
                if (is_sign_show || is_num_show || is_point_show) {
                    // cout << " sign 2";
                    return false;
                } 
                is_sign_show = true;
                continue;
            }
            if (s[i] == '.') {
                if (end == start) return false; // "." one special case
                if (is_point_show) {
                    // cout << " point 2";
                    return false;
                }
                is_point_show = true;
                continue;
            }
            if (!isdigit(s[i])) {
                // cout << " not nnmber s[i] = " << s[i] << endl;
                return false;
            }
            is_num_show = true;
        }
        if (end - start > 0 && !is_num_show)
            return false;
        return i == end + 1;
    }

    bool is_int(string s) {
        if (s.empty())
            return false;

        int start = 0, end = s.size() - 1;
        while (s[start] == ' ') ++start;
        while (s[end] == ' ') --end;
        if (start == end + 1)
            return false;   // 只有空格

        bool is_sign_show = false;
        bool is_num_show = false;
        int i = start;
        for (; i <= end; i++) {
            if (s[i] == '+' || s[i] == '-') {
                if (end == start) return false;
                if (is_sign_show || is_num_show) {
                    return false;
                } 
                is_sign_show = true;
                continue;
            }
            if (!isdigit(s[i]))
                return false;
            is_num_show = true;
        }
        return i == end + 1;
    }
public:
    bool isNumber(string s) {
        if (s.empty())
            return false;
        int e_idx = 0;
        for (; s[e_idx]; ++e_idx) {
            if (s[e_idx] == 'e')
                break;
        }
        if (e_idx < s.size()) {
            return is_float(s.substr(0, e_idx)) && is_int(s.substr(e_idx + 1));
        }
        return is_float(s) || is_int(s);
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

