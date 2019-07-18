class Solution {
    void combinationSum(vector<int> &nums, int target, int begin, vector<int> &combination, vector<vector<int>> &res){
        if(!target){
            res.push_back(combination);
            return;
        }
        for(int i = begin; i < nums.size() && target >= nums[i]; ++i){
            combination.push_back(nums[i]);
            combinationSum(nums, target-nums[i], i, combination, res);
            combination.pop_back();
        }
    }
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        vector<int> combination;
        sort(candidates.begin(), candidates.end());
        combinationSum(candidates, target, 0, combination, res);
        return res;
    }
};