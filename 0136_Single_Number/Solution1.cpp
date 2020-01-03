#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int res = 0;
        for (int i : nums)
            res ^= i;
        return res;
    }
};

void test(string test_name, vector<int> &nums, int expected)
{
    if (Solution().singleNumber(nums) == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    vector<int> nums1 = {2,2,1};
    int expected1 = 1;
    test("test1", nums1, expected1);

    vector<int> nums2 = {4,1,2,1,2};
    int expected2 = 4;
    test("test2", nums2, expected2);

    return 0;
}
