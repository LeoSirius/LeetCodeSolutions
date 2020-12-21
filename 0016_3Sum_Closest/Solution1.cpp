#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int res = nums[0] + nums[1] + nums[2];
        for (int i = 1; i < nums.size() - 2; i++) {
            int l = i + 1, r = nums.size() - 1;
            while (l < r) {
                int sum = nums[i] + nums[l] + nums[r];
                if (sum == target)
                    return target;
                res = abs(target-sum) < abs(target-res) ? sum : res;
                if (sum < target)
                    l++;
                else
                    r--;
            }
        }
        return res;
    }
};


void test(string test_name, vector<int> &nums, int target, int expected)
{
    int res = Solution().threeSumClosest(nums, target);
    cout << "res = " << res << endl;
    if (res == expected) {
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
