#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

class Solution {
    void subsets(vector<int> &nums, int i, vector<int> &sub, vector<vector<int>> &subs)
    {
        subs.push_back(sub);
        for (int j = i; j < nums.size(); j++) {
            sub.push_back(nums[j]);
            subsets(nums, j + 1, sub, subs);
            sub.pop_back();
        }
    }
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> subs;
        vector<int> sub;
        subsets(nums, 0, sub, subs);
        return subs;
    }
};

void test(string test_name, vector<int> &nums, vector<vector<int>> &expected)
{
    Solution s;
    vector<vector<int>> res = s.subsets(nums);
    for (int i = 0; i < res.size(); i++) {
        sort(res[i].begin(), res[i].end());
    }
    sort(res.begin(), res.end());

    for (int i = 0; i < expected.size(); i++) {
        sort(expected[i].begin(), expected[i].end());
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
    vector<int> nums1 = {1,2,3};
    vector<vector<int>> expected1 = {
        {},{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}
    };
    test("test1", nums1, expected1);

    return 0;
}
