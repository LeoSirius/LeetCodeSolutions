#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int findRepeatNumber(vector<int>& nums) {
        for (int i=0;i<nums.size();i++) {
            while(nums[i] != i){
                // 如果有重复的数，返回
                if(nums[nums[i]] == nums[i])
                    return nums[i];
                // 把nums[i]的值(k)放到值所在索引(k)的位置上
                swap(nums[nums[i]], nums[i]);
            }
        }
        return -1;
    }
};

void test(string test_name, vector<int>& nums, vector<int> expected)
{
    int res = Solution().findRepeatNumber(nums);
    cout << "res = " << res << endl;
    if (find(expected.begin(), expected.end(), res) != expected.end())
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    vector<int> nums1 = {2, 3, 1, 0, 2, 5, 3};
    vector<int> expected1 = {2, 3};
    test("test1", nums1, expected1);

    vector<int> nums2 = {0, 1, 2, 3, 4, 11, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15};
    vector<int> expected2 = {11};
    test("test2", nums2, expected2);
}
