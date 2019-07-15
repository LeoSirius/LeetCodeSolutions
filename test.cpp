class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int> res = {-1, -1};
        if(nums.size() == 0){
            return res;
        }
        int left = 0, right = nums.size()-1;
        while(left < right){
            int mid = (left + right) / 2;
            if(nums[mid] < target) left = mid + 1;
            else right = mid;
        }
        if(nums[left] != target) return res;    // target不在nums中
        else res[0] = left;

        right = nums.size() - 1;  // left不用重置
        while(left < right){
            int mid = (left + right) / 2 + 1;  // +1 make mid biased to right
            if(target < nums[mid]) right = mid - 1;
            else left = mid;
        }
        res[1] = right;
        return res;
    }
};