#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        vector<int> res;
        int carry = 0;
        for (int i = digits.size() - 1; i >= 0; i--) {
            int sum = digits[i] + carry;
            if (i == digits.size() - 1) {
                sum += 1;
            }
            res.insert(res.begin(), sum % 10);
            carry = sum / 10;
        }
        if (carry) {
            res.insert(res.begin(), carry);
        }
        return res;
    }
};

void test(string test_name, vector<int> &digits, vector<int> &expected)
{
    Solution s;
    if (s.plusOne(digits) == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    vector<int> digits1 = {1,2,3};
    vector<int> expected1 = {1,2,4};
    test("test1", digits1, expected1);

    vector<int> digits2 = {4,3,2,1};
    vector<int> expected2 = {4,3,2,2};
    test("test2", digits2, expected2);

    vector<int> digits3 = {9};
    vector<int> expected3 = {1,0};
    test("test3", digits3, expected3);

    return 0;
}

