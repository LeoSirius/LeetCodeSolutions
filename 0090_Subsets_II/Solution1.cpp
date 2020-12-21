#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

class Solution {
    void subsets(vector<int> &nums, int begin, vector<int> &sub, vector<vector<int>> &subs)
    {
        subs.push_back(sub);
        for (int i = begin; i < nums.size(); i++) {
            if (i > begin && nums[i] == nums[i-1])
                continue;
            sub.push_back(nums[i]);
            subsets(nums, i+1, sub, subs);
            sub.pop_back();
        }
    }
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<int> sub;
        vector<vector<int>> subs;
        sort(nums.begin(), nums.end());
        subsets(nums, 0, sub, subs);
        return subs;
    }
};

void test(string test_name, vector<int> &nums, vector<vector<int>> &expected)
{
    Solution s;
    vector<vector<int>> res = s.subsetsWithDup(nums);
    for (auto item : res) {
        sort(item.begin(), item.end());
    }
    sort(res.begin(), res.end());
    for (auto item : expected) {
        sort(item.begin(), item.end());
    }
    sort(expected.begin(), expected.end());

    if (res == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    vector<int> nums1 = {1,2,2};
    vector<vector<int>> expected1 = {
        {},{1},{2},{1,2},{2,2},{1,2,2}
    };
    test("test1", nums1, expected1);

    vector<int> nums2 = {4,4,4,1,4};
    vector<vector<int>> expected2 = {
        {},{1},{1,4},{1,4,4},{1,4,4,4},{1,4,4,4,4},{4},{4,4},{4,4,4},{4,4,4,4}
    };
    test("test2", nums2, expected2);

    return 0;
}
