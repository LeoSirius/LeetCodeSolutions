class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int length = nums.size();
        if(length == 0){
            return 0;
        }
        int new_tail = 0;
        for(int i = 0; i < length; i++){
            if(nums[i] != val){
                nums[new_tail++] = nums[i];
            }
        }
        return new_tail;
    }
};