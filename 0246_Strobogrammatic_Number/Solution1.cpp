#include <iostream>
#include <unordered_map>
using namespace std;

class Solution {
public:
    bool isStrobogrammatic(string num) {
        unordered_map<int, int> mapping = {{0,0}, {1,1}, {6,9}, {8,8}, {9,6}};
        int l = 0, r = num.size() - 1;
        while (l < r) {
            if (num[l++] - '0' != mapping[num[r--] - '0'])
                return false;
        }
        if (l == r) {
            int val = num[l] - '0';
            return val == 0 || val == 1 || val == 8;
        }
        return true;
    }
};

void test(string test_name, string num, bool expected)
{
    bool res = Solution().isStrobogrammatic(num);
    if (res == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    string num1 = "69";
    bool expected1 = true;
    test("test1", num1, expected1);

    string num2 = "88";
    bool expected2 = true;
    test("test2", num2, expected2);

    string num3 = "962";
    bool expected3 = false;
    test("test3", num3, expected3);

    return 0;
}
