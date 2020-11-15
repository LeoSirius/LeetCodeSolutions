#include <iostream>
#include <deque>
using namespace std;

class Solution {
public:
    string removeKdigits(string num, int k) {
        if (k == num.size())
            return "0";
        deque<char> deq;
        for (int i = 0; i < num.size(); i++) {
            while (k && !deq.empty() && num[i] < deq.back()) {
                deq.pop_back();
                k--;
            }
            deq.push_back(num[i]);
        }

        //56789这种情况，前面一直比后面小，
        while(k>0)
        {
            k--;
            deq.pop_back();
        }

        string res = "";
        while (!deq.empty()) {
            res += deq.front();
            deq.pop_front();
        }

        int start = 0;
        // start < res.size() - 1  减一是为了处理10000这种情况，需要返回一个0
        while (start < res.size() - 1 && res[start] == '0')
            start++;
        return res.substr(start);
    }
};

void test(string test_name, string num, int k, string expected)
{
    string res = Solution().removeKdigits(num, k);
    if (res == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    string num1 = "1432219";
    int k1 = 3;
    string expected1 = "1219";
    test("test1", num1, k1, expected1);

    string num2 = "10200";
    int k2 = 1;
    string expected2 = "200";
    test("test2", num2, k2, expected2);

    string num3 = "10";
    int k3 = 2;
    string expected3 = "0";
    test("test3", num3, k3, expected3);

    string num4 = "10";
    int k4 = 1;
    string expected4 = "0";
    test("test4", num4, k4, expected4);

    string num5 = "100";
    int k5 = 1;
    string expected5 = "0";
    test("test5", num5, k5, expected5);

    string num6 = "112";
    int k6 = 1;
    string expected6 = "11";
    test("test6", num6, k6, expected6);


    return 0;
}

// Given a non-negative integer num represented as a string,
//  remove k digits from the number so that the new number is the smallest possible.

// Note:
// The length of num is less than 10002 and will be ≥ k.
// The given num does not contain any leading zero.

// Example 1:
// Input: num = "1432219", k = 3
// Output: "1219"
// Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

// Example 2:
// Input: num = "10200", k = 1
// Output: "200"
// Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

// Example 3:
// Input: num = "10", k = 2
// Output: "0"
// Explanation: Remove all the digits from the number and it is left with nothing which is 0.

