#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        int closest = nums[0] + nums[1] + nums[2];
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size(); i++) {
            int left = i + 1, right = nums.size() - 1;
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                if (sum > target) {
                    right--;
                } else if (sum < target) {
                    left++;
                } else {
                    return sum;
                }
                if (abs(sum - target) < abs(closest - target)) {
                    closest = sum;
                }
            }

        }
        return closest;
    }
};

void test(string test_name, vector<int> &nums, int target, int expected)
{
    Solution s;
    if (s.threeSumClosest(nums, target) == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    vector<int> nums1 = {-1, 2, 1, -4};
    int target1 = 1;
    int expected1 = 2;
    test("test1", nums1, target1, expected1);
    return 0;
}