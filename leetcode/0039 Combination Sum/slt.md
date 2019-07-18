### 思路1 DFS

```cpp
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
```

```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res
        
    def dfs(self, nums, target, index, path, res):
        if target < 0:
            return # backtracking
        if target == 0:
            res.append(path)
            return
        for i in range(index, len(nums)):
            self.dfs(nums, target-nums[i], i, path+[nums[i]], res)
```