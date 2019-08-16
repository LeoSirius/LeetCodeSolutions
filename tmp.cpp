class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> my_map;
        vector<int> res;
        int size = nums.size();
        for(int i = 0; i < size; i++){
            int num_fo_find = target - nums[i];