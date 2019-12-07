### 思路1 DFS

```cpp
class Solution {
    void combinationSum(vector<int> &nums, int target, int begin, vector<int> &path, vector<vector<int>> &res){
        if(!target){
            res.push_back(path);
            return;
        }
        for(int i = begin; i < nums.size() && target >= nums[i]; ++i){
            path.push_back(nums[i]);
            combinationSum(nums, target-nums[i], i, path, res); // 一个元素可以用多次，所以i不变。组合不用检查，因为candidates里面没有重复的元素
            path.pop_back();
        }
    }
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        vector<int> path;
        sort(candidates.begin(), candidates.end());
        combinationSum(candidates, target, 0, path, res);
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