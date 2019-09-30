#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            while (nums[i] >= 1 && nums[i] <= n && nums[nums[i] - 1] != nums[i]) {
                swap(nums[nums[i] - 1], nums[i]);
            }
        }
        for (int i = 0; i < n; i++) {
            if (nums[i] != i + 1)
                return i + 1;
        }
        return n + 1;
    }
};

// test code

string test1() {
    Solution s;
    vector<int> nums{3, 4, -1, 1};
    int expected_output = 2;
    if (s.firstMissingPositive(nums) == expected_output) {
        return "success";
    } else {
        return "fail";
    }
}

int main()
{
    cout << "test1:\n" << test1() << "\n\n";
    return 0;
}