class Solution {
    void dfs(vector<int>& nums, int target, int begin, vector<int>& path, vector<vector<int>>& res){
        if(!target){
            res.push_back(path);
            return;
        }
        for(int i = begin; i < nums.size() && target >= nums[i]; i++){
            if(i > begin && nums[i] == nums[i-1]) continue;
            path.push_back(nums[i]);
            dfs(nums, target - nums[i], i + 1, path, res);
            path.pop_back();
        }
    }
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        vector<int> path;
        sort(candidates.begin(), candidates.end());
        dfs(candidates, target, 0, path, res);
        return res;
    }
};