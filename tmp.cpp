class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int>> res;
        if (nums.size() < 4) return res;
        sort(nums.begin(), nums.end());

        for (int i = 0; i < nums.size() - 3; i++) {
            if (i > 0 && nums[i] == nums[i-1]) continue;
            int three_target = target - nums[i];

            for (int j = i + 1; j < nums.size() - 2; j++) {
                if (j > i+1 && nums[j] == nums[j-1]) continue;
                int two_target = three_target - nums[j];
                int l, r;
                l = j + 1; r = nums.size() - 1;
                while (l < r) {
                    int left, right;
                    left = nums[l];;
                    right = nums[r];
                    if (left + right == two_target) {
                        res.push_back(vector<int> {nums[i], nums[j], left, right});
                        while (l < r && nums[l] == left) l++;
                        while (l < r && nums[r] == right) r--; 
                    } else if (left + right < two_target) l++;
                    else r--;
                }
            }
        }
        return res;
    }
};