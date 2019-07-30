class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int len = nums.size();
        if(!len) return -1;
        int left, right, mid;
        left = 0, right = len - 1;
        while(left <= right){
            mid = left + (right - left) / 2;
            if(nums[mid] == target) return mid;
            else if(target > nums[mid]) left = mid + 1;
            else right = mid - 1;
        }
        return left;
    }
};