#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int closest = nums[0] + nums[1] + nums[2];
        for (int i = 0; i < nums.size() - 2; i++) {
            int left = i + 1, right = nums.size() - 1;
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                if (sum == target) {
                    return sum;
                } else if (sum > target) {
                    right--;
                } else {
                    left++;
                }
                if (abs(sum - target) < abs(closest - target))
                    closest = sum;
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


    vector<int> nums2 = {1,1,1,0};
    int target2 = -100;
    int expected2 = 2;
    test("test2", nums2, target2, expected2);

    vector<int> nums3 = {-3,-2,-5,3,-4};
    int target3 = -1;
    int expected3 = -2;
    test("test3", nums3, target3, expected3);

    return 0;
}
