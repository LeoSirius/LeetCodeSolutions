#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int res = 0;
        unordered_map<int, int> mp; // key是nums中的数，value是数所在的streak的长度
        for (auto n : nums) {
            if (mp.find(n) != mp.end())
                continue;
            // 如果左右两侧在dict中，则获取左右两侧区间的长度
            int left_len = mp.find(n-1) != mp.end() ? mp[n-1] : 0;
            int right_len = mp.find(n+1) != mp.end() ? mp[n+1] : 0;

            int cur_len = left_len + right_len + 1;
            res = max(res, cur_len);
            // 更新左右端点，和当前的n为这个区间的长度
            mp[n] = cur_len;
            mp[n-left_len] = cur_len;
            mp[n+right_len] = cur_len;
        }
        return res;
    }
};

void test(string test_name, vector<int>& nums, int expected)
{
    int res = Solution().longestConsecutive(nums);
    if (res == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    vector<int> nums1 = {100, 4, 200, 1, 3, 2};
    int expected1 = 4;
    test("test1", nums1, expected1);

    vector<int> nums2 = {0,3,7,2,5,8,4,6,0,1};
    int expected2 = 9;
    test("test2", nums2, expected2);


    vector<int> nums3 = {4,0,-4,-2,2,5,2,0,-8,-8,-8,-8,-1,7,4,5,5,-4,6,6,-3};
    int expected3 = 5;
    test("test3", nums3, expected3);

    return 0;
}