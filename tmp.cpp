class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> res;
        for (int i = 0; i < nums.size(); i++) {
            if (i > 0 && nums[i] == nums[i-1]) continue;
            int l, r;
            l = i + 1; r = nums.size() - 1;
            while (l < r) {
                int left, right;
                left = nums[l]; right = nums[r];
                int sum = nums[i] + left + right;
                if (sum == 0) {
                    res.push_back(vector<int> {nums[i], left, right});
                    while (l < r && nums[l] == left) l++;
                    while (l < r && nums[r] == right) r--;
                } else if(sum > 0) {
                    r--;
                } else {
                    l++;
                }
            }
        }
        return res;
    }
};